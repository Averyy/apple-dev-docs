# Integrating your messaging app with Apple Intelligence

**Framework**: App Intents

Adopt message schemas so people can send messages and manage conversations with Siri.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

UnicornChat is a SwiftUI app for iPhone, iPad, and Mac that lets people send messages to predefined, fictitious unicorn characters. People can message an individual unicorn or a group of unicorns; the unicorns respond with friendly and upbeat messages. The app supports common message actions like drafting and sending a message, adding a message attachment, editing a message, unsending a message, and reacting to a message.

In addition to providing functionality in the app, this sample code project makes its content and actions discoverable by Apple Intelligence and allows people to:

- Find messages and contacts from the app in Spotlight.
- Use Siri to perform app actions like drafting and sending a message or reacting to a message using natural language.
- Create custom shortcuts in the Shortcuts app.
- Place an App Shortcut on the Action button or the Home Screen.

> **Note**: This sample code project is associated with WWDC26 session [`240: Build intelligent Siri experiences with App Schemas`](https://developer.apple.comhttps://developer.apple.com/wwdc26/240/).

#### Conform Entities to App Schemas

App data is private to the app and Apple Intelligence doesn’t have access to the app’s functionality or context about its content. For example, when a person says “Siri, send a message to Bubbles,” Apple Intelligence needs to resolve that Bubbles is a contact in the UnicornChat app, that UnicornChat is a messaging app that supports a set of defined messaging actions, and that its data is contacts and messages.

To enable Apple Intelligence to find and resolve references to app content, the app provides structured representations of its data in the form of [`AppEntity`](appentity.md) implementations that conform to app schemas. *App entities* are lightweight representations of the app’s data-model objects that contain the information Apple Intelligence and system experiences such as Siri need. *App schemas* add structure to the app’s actions and content, enabling Apple Intelligence to interpret natural language, recognize onscreen context, and disambiguate vague requests.

This code snippet shows how the app’s `MessageEntity` conforms to the [`message`](appschema/messagesentity/message.md) entity schema, including all properties that the schema requires. Note how `MessageEntity` provides a custom display representation to enable the system to show a rich representation of the entity. The conformance to [`IndexedEntity`](indexedentity.md) isn’t part of the schema conformance, but is a prerequisite for making message entities available in Spotlight, as described in [`Index entities in Spotlight`](integrating-your-messaging-app-with-apple-intelligence#Index-entities-in-Spotlight.md).

```swift
@AppEntity(schema: .messages.message)
struct MessageEntity: IndexedEntity {
    
    // MARK: Static
    
    static let defaultQuery = MessageQuery()
    
    // MARK: Properties
    
    var id: UUID
    
    /// The type of message.
    var messageType: MessageType
    
    /// The author of this message.
    var author: ContactEntity
    
    /// A Boolean value that indicates whether the recipient read this message.
    var isRead: Bool
    
    /// A set of attributes that describe this message's state.
    var attributes: Set<MessageAttribute>
    
    /// The conversation that contains this message.
    var conversation: ConversationEntity
    
    /// The send or receive date for this message.
    /// For a scheduled message, this represents the scheduled send date.
    var date: Date
    
    /// The subject line, when available.
    var subject: AttributedString?
    
    /// The text content of the message.
    var body: AttributedString?
    
    /// File attachments that the message contains.
    var attachments: [IntentFile]
    
    /// An audio recording that accompanies the message.
    var audioMessage: IntentFile?
    
    /// Attachments that don't conform to uniform type identifiers.
    var customAttachments: [CustomAttachment]
    
    /// Location data that the message contains.
    var locations: [PlaceDescriptor]
    
    /// Any detected links in the message.
    var links: [LinkPresentation.LinkMetadata]
    
    /// A message effect for this message.
    var messageEffect: MessageEffect?
    
    /// A custom reaction for this message.
    var reaction: MessageReaction?
    
    /// The parent message for a thread or reaction.
    var referencedMessage: MessageEntity?
    
    /// An identifier the system associates with this message
    /// for notification announcements.
    var notificationIdentifier: String?
    
    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(
            title: "\(body ?? "")",
            subtitle: "\(conversation.displayName)",
            image: attachments.reduce(into: conversation.image) { image, file in
                image = DisplayRepresentation.Image(data: file.data)
            }
        )
    }
    
    // ...
}
```

To enable the system to query the app for message entities, its [`EntityQuery`](entityquery.md) implementation finds entities using a simple identifier lookup:

```swift
extension MessageEntity {
    struct MessageQuery: EntityQuery {
        @Dependency
        var model: ModelManager

        func entities(for identifiers: [MessageEntity.ID]) async throws -> [MessageEntity] {
            try await model.messageEntities(for: identifiers)
        }
        
        // Implement this callback to provide suggested entities in the Shortcuts app.
        func suggestedEntities() async throws -> [MessageEntity] {
            try await model.fetchRecentMessageEntities(limit: 5)
        }
    }
}
```

The [`EntityQuery`](entityquery.md) implementation also implements the optional [`suggestedEntities()`](entityquery/suggestedentities().md) callback to return the most recent messages in the Shortcuts app.

Because the `MessageEntity` conforms to the `message` app schema, the app also has to implement supporting entity and enum types that also conform to app schemas. For example, it defines a `CustomAttachment` entity:

```swift
@AppEntity(schema: .messages.customAttachment)
struct CustomAttachment: AppEntity {
    static let defaultQuery = CustomAttachmentQuery()

    var id: UUID

    /// The source plugin for this attachment.
    var sourceName: AttributedString?

    /// A description the system presents in a dialog for this attachment.
    var description: AttributedString?

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(
            title: "\(description ?? "")"
        )
    }

    struct CustomAttachmentQuery: EntityQuery {
        func entities(for identifiers: [CustomAttachment.ID]) async throws -> [CustomAttachment] {
            // The app doesn't support custom attachments for messages, returning an empty
            // array.
            []
        }
    }
}
```

For more information about creating app entities and implementing app schemas, see [`Defining app entities for your custom data types`](defining-app-entities-for-your-custom-data-types.md) and [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).

#### Make Entities Transferable

In addition to conforming entities to an app schema, the app’s entities also conform to the [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) protocol. This enables Apple Intelligence to pass the message entities to other apps and system experiences.

```swift
extension MessageEntity: Transferable {

    static var transferRepresentation: some TransferRepresentation {
        DataRepresentation(exportedContentType: .png) { message in
            message.attachments.first?.data ?? Data()
        }
        .exportingCondition { $0.attachments.first != nil }
    }
}

```

#### Index Entities in Spotlight

Apple Intelligence uses the semantic search capabilities of Spotlight to find the app’s content, even when someone describes it vaguely. The following example shows how the app loads entities that represent contacts, conversations, and messages, then donates them to the Spotlight index:

```swift
func storeDidFinishLaunching() async throws {
    // ...

    // Fetch entities.
    let contactEntities = try fetchRecentContacts(limit: nil).map(\.entity)
    let conversationEntities = try fetchRecentConversations(limit: nil).map(\.entity)
    let messageEntities = try fetchRecentMessages(limit: nil).map(\.entity)

    // Index content to Spotlight.
    try? await CSSearchableIndex.default().indexAppEntities(contactEntities)
    try? await CSSearchableIndex.default().indexAppEntities(conversationEntities)
    try? await CSSearchableIndex.default().indexAppEntities(messageEntities)

    // ...
}
```

For more information about making app content available to Spotlight, see [`Spotlight integration`](spotlight.md).

#### Annotate Views and Notifications with App Entities

People use Siri to interact with onscreen content. For example, someone might say “Siri, summarize this message.” To fulfill the request, Apple Intelligence needs contextual information about content that’s visible onscreen. To provide the needed context, the sample app annotates its view with app entities that represent the onscreen content. For example, the app’s `MessageRow` view annotates its [`HStack`](https://developer.apple.com/documentation/swiftui/hstack) with an app entity using the [`appEntityIdentifier(_:)`](https://developer.apple.com/documentation/swiftui/view/appentityidentifier(_:)) modifier:

```swift
var body: some View {
    HStack(alignment: .lastTextBaseline, spacing: 0) {
        // ...
    }
    .frame(maxWidth: .infinity, alignment: isMe ? .trailing : .leading)
    .listRowSeparator(.hidden)
    .listRowInsets(EdgeInsets())
    .padding(.horizontal)
    .padding(.vertical, 4)
    .task(id: message) {
        await markMessageAsRead(message)
    }
    .appEntityIdentifier(EntityIdentifier(for: MessageEntity.self, identifier: message.id))
}
```

To provide Apple Intelligence with context about a local notification and allow it to respond to requests like “Siri, reply to this message,” the sample also associates the notification with app entities:

```swift
func scheduleNotification(for message: Message, from author: Contact, in conversation: Conversation) {
    let content = UNMutableNotificationContent()
    content.title = author.name
    content.body = message.body
    content.sound = .default
    content.threadIdentifier = conversation.id.uuidString
    content.categoryIdentifier = "MESSAGE_CATEGORY"
    content.appEntityIdentifiers = [
        EntityIdentifier(for: MessageEntity.self, identifier: message.id)
    ]

    // ...    
}
```

For more information about providing Apple Intelligence with onscreen context by associating app entities with views and other types, see [`Providing contextual cues to Apple Intelligence and Siri`](providing-contextual-cues-to-apple-intelligence-and-siri.md).

#### Make Actions Discoverable By Apple Intelligence and Siri

UnicornChat makes its message actions discoverable by implementing the app intent schemas from the messages domain. Similar to how entity schemas provide Apple Intelligence with an understanding of the app’s content, intent schemas provide Apple Intelligence with an understanding of the app’s message actions. The [`Messages`](app-schema-domain-messages.md) domain requires several intents to provide a consistent user experience. The example below shows the intent for sending a message. It conforms to the `.messages.sendMessage` schema. The example also shows the implementation of the required `MessageDestination` union value type that the `destination` property uses:

```swift
import AppIntents
import GeoToolbox
import SwiftData
import UniformTypeIdentifiers

typealias Recipients = [ContactEntity]

@UnionValue
enum MessageDestination {
    case contact(ContactEntity)
    case recipients(Recipients)

    var persons: [ContactEntity] {
        switch self {
        case let .contact(contact):
            return [contact]
        case let .recipients(recipients):
            return recipients
        }
    }
}

@AppIntent(schema: .messages.sendMessage)
struct SendMessageIntent: AppIntent {
    var destination: MessageDestination
    var subject: AttributedString?
    var content: AttributedString?
    @Parameter(supportedContentTypes: [.image]) var attachments: [IntentFile]
    @Parameter(supportedContentTypes: [.audio]) var audioMessage: IntentFile?
    var locations: [PlaceDescriptor]
    var links: [URL]
    var scheduledDate: Date?

    @Dependency
    var model: ModelManager

    // MARK: Methods

    func perform() async throws -> some ReturnsValue<[MessageEntity]> {
        let recipientIDs = destination.persons.map(\.id)
        let messageText = content.flatMap { String($0.characters) } ?? ""
        let messageIDs = try await model.sendMessage(toRecipientIDs: recipientIDs,
                                                     conversationID: nil,
                                                     messageText: messageText,
                                                     attachments: attachments)
        let messages = try await model.messageEntities(for: messageIDs)
        return .result(value: messages)
    }
}
```

For more information about making actions discoverable by Apple Intelligence, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).

#### Donate App Intents to the System

Apple Intelligence can proactively suggest actions based on a person’s past behavior. For example, if a person messages the same contact every morning, Apple Intelligence might proactively suggest the action each morning. The following example shows how the app uses the [`IntentDonationManager`](intentdonationmanager.md) structure to donate a `SendMessageIntent` when a person sends a message:

```swift
@discardableResult
func sendMessage(
    toRecipientIDs recipientIDs: [Contact.ID],
    conversationID: Conversation.ID? = nil,
    messageText: String,
    attachments: [IntentFile] = [],
    donateIntent: Bool = false
) async throws -> [Message.ID] {
     // ...

    if donateIntent {
        let intent = SendMessageIntent()
        intent.destination = .recipients(conversation.recipients.map(\.entity))
        intent.content = AttributedString(messageText)
        let result = messages.map(\.entity)

        // Donate the intent so the system can improve future suggestions.
        Task {
            do {
                try await IntentDonationManager.shared.donate(intent: intent, result: .result(value: result))
            } catch {
                print("Failed to donate intent: \(error)")
            }
        }
    }

    // ...
}
```

For more information about donating actions and content to the system, see [`Donations and discovery`](donations-and-discovery.md).

## See Also

- [Integrating your calendar app with Apple Intelligence](integrating-your-calendar-app-with-apple-intelligence.md)
  Adopt calendar schemas so people can create, find, and manage events with Siri.
- [Integrating your music app with Apple Intelligence](integrating-your-music-app-with-apple-intelligence.md)
  Adopt the audio and clock schemas so people can play music and set alarms with Siri.
- [Integrating your photo app with Apple Intelligence](integrating-your-photo-app-with-apple-intelligence.md)
  Adopt photo schemas so people can edit and manage photos with Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/integrating-your-messaging-app-with-apple-intelligence)*