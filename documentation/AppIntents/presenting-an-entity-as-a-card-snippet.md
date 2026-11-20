# Presenting an entity as a card snippet

**Framework**: App Intents  
**Role**: Article

Show a custom view of your app’s content in system experiences such as Siri responses and conversation transcripts.

## Overview

When your app’s content appears outside your app in a system experience, such as a Siri response or a conversation transcript, the system represents an app entity as a [`DisplayRepresentation`](./displayrepresentation.md) by default. The system’s default display representation includes a title, a subtitle, and an image to help identify the content, but your app doesn’t control its layout.

Your app can provide a richer experience by giving an entity a *card snippet*, a custom SwiftUI view for a specific entity. For contexts that the card supports, the system shows the card snippet instead of the default display representation. For example, a messaging app can show a message as a card with the sender, the message text, and a control that marks the message as read.

The system can present the card when your app isn’t actively running because it renders the view ahead of time. That behavior can affect how your app builds the view and when it updates an entity’s properties.

The *UnicornChat* sample app includes a card snippet implementation; see [Integrating your messaging app with Apple Intelligence](./integrating-your-messaging-app-with-apple-intelligence.md).

## Add a card to an entity

You can replace the system’s default display representation with a custom view. Conform an entity type to [`SnippetRepresentableEntity`](./snippetrepresentableentity.md) by adding a [`snippet`](./snippetrepresentableentity/snippet-swift.type.property.md) property that returns a [`CardSnippet`](./cardsnippet.md).

```swift
import AppIntents
import SwiftUI

extension MessageEntity: SnippetRepresentableEntity {
    static var snippet: some Snippet {
        CardSnippet(supportedFamilies: [.standard]) { message, context in
            MessageSnippetCard(message: message)
        }
    }
}
```

The [`CardSnippet`](./cardsnippet.md) initializer’s `supportedFamilies` parameter is an array of [`CardSnippetFamily`](./cardsnippetfamily.md) options that represent what your card implementation can adapt to. In this example, the card snippet only includes the [`standard`](./cardsnippetfamily/standard.md) option, which means the implementation supports only a full-size card.

> **Note**: The system shows the entity’s default display representation for the families your card doesn’t support.

Your card can support additional snippet family options, such as [`compact`](./cardsnippetfamily/compact.md), by adapting the view’s layout to the available space, as the *UnicornChat* sample does.

## Build the card from static content

The system renders the card ahead of time and keeps it in a static archive, which means the view can’t change after the system captures it. Your app needs to build the card from content that’s ready when it creates the view, such as text and images.

> 💡 **Tip**: Include only content that’s appropriate to appear in a system experience, because the system can show the card outside your app.

Before you create the view, prepare any data it depends on: store formatted text in an entity property, and create any images synchronously.

For example, the following view shows a message along with the time and the sender’s name:

```swift
struct MessageSnippetCard: View {
    let message: MessageEntity

    var body: some View {
        VStack(alignment: .leading) {
            HStack(alignment: .firstTextBaseline) {
                Text(message.author.person.displayName)
                    .bold()
                    .foregroundStyle(message.isRead ? .secondary : .primary)
                    .lineLimit(1)
                Spacer()
                Text(message.date, style: .time)
                    .font(.footnote)
                    .foregroundStyle(.secondary)
            }
            Text(message.body ?? "")
                .foregroundStyle(.secondary)
        }
    }
}
```

The card snippet presents the entity’s current information based on its properties. The card also has access to the standard SwiftUI environment values, such as the color scheme and locale, through the `@Environment` property wrapper.

> ❗ **Important**: The system captures the view as a snapshot in time, so a card that depends on content that arrives after capture, such as an `AsyncImage` or a later `@State` change, might show stale or missing information.

You can configure a custom background for a card by passing the [`cardSnippet`](../SwiftUI/containerbackgroundplacement/cardsnippet.md) placement to the [`containerBackground(_:for:)`](../SwiftUI/view/containerbackground%28_,for%29.md) view modifier.

## Add actions with app intents

A card can also let someone act without opening your app. Add a SwiftUI control that runs an app intent, such as a `Button` or `Toggle`. When a person interacts with the control, the system runs the intent and creates a new version of the card that reflects the change.

For example, the following card adds a button that toggles the state of the message between “Read” and “Unread” by running the app’s `SetMessageReadStatusIntent`:

```swift
struct MessageSnippetCard: View {
    let message: MessageEntity

    private var toggleReadStatusIntent: SetMessageReadStatusIntent {
        let intent = SetMessageReadStatusIntent()
        intent.message = message
        intent.isRead = !message.isRead
        return intent
    }

    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            Button(intent: toggleReadStatusIntent) {
                Label(
                    message.isRead ? "Mark as Unread" : "Mark as Read",
                    systemImage: message.isRead ? "largecircle.fill.circle" : "circle"
                )
                .labelStyle(.iconOnly)
                .contentTransition(.symbolEffect(.replace))
            }
            .buttonStyle(.plain)

            // The message layout from the previous step.
        }
    }
}
```

When someone taps the button, the system invokes the `SetMessageReadStatusIntent`. That intent updates the message’s `isRead` state and returns an entity that reflects the message’s new state. The system renders the card again, which updates the button’s icon.

> **Note**: The button hides its label text with an icon-only style, but the title still serves as the button’s accessibility label, so VoiceOver announces the action.

The view animates the difference between the two versions by adding a [`contentTransition(_:)`](../SwiftUI/view/contenttransition%28_%29.md) view modifier to the control.

## Open your app from the card

In addition to a card’s controls, someone can also tap the card itself. Tapping the card opens your app by default, but your app can open to something specific by adopting the [`open`](./appschema/systemintent/open.md) schema in the system domain. For example, the UnicornChat sample has an `OpenConversationIntent` type that adopts the `.system.open` schema by conforming to the [`OpenIntent`](./openintent.md) protocol:

```swift
@AppIntent(schema: .system.open)
struct OpenConversationIntent: OpenIntent {
    static let title: LocalizedStringResource = "Open Conversation"

    @Parameter
    var target: ConversationEntity

    @Dependency
    var navigation: NavigationManager

    @MainActor
    func perform() async throws -> some IntentResult {
        navigation.openConversation(for: target)
        return .result()
    }
}
```

When someone taps the card, the system runs the intent instead of opening your app directly.

> 💡 **Tip**: You can add an open intent for each entity type that represents specific content you want your app to navigate to when someone taps that entity’s card.

## See Also

### Card snippets
- [protocol SnippetRepresentableEntity](./snippetrepresentableentity.md)
  An app entity that provides a visual representation for its content.
- [struct CardSnippet](./cardsnippet.md)
  A type that presents the SwiftUI view for an app entity as a card.
- [struct CardSnippetContext](./cardsnippetcontext.md)
  A type that stores information about how to render a card snippet.
- [struct CardSnippetFamily](./cardsnippetfamily.md)
  A type that defines the supported rendering environments for card snippets.
- [protocol EntitySnippetContent](./entitysnippetcontent.md)
  A visual representation that the system renders for an entity.
- [enum EntitySnippetContentBuilder](./entitysnippetcontentbuilder.md)
  A result builder that assembles an entity’s snippet declarations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/presenting-an-entity-as-a-card-snippet)*