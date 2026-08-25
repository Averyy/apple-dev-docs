# Providing contextual cues to Apple Intelligence and Siri

**Framework**: App Intents

Annotate your interface with app entities to offer contextual information about your app’s onscreen content.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+
- Xcode 16.2+

#### Overview

Your app’s interface reflects what a person is doing, and what data they’re viewing or changing. Although your app’s interface contains data, the system can’t use that data directly because it’s private to your app. However, you can annotate views and other content with app entities to give the system the context it needs to improve other types of interactions. For example, when someone refers to parts of your app’s content during a Siri conversation, Apple Intelligence can use the contextual information you provide to understand what the person meant.

##### Apply a Domain Specific Schema to Your Custom Type

The App Intents framework defines domains for different types of content, and schemas for the app intents and app entities related to those domains. Each schema specifies the expected format for app intents and entities, including any expected parameters or properties. If your content matches one of the existing schemas, apply that schema to your type and implement the required content.

> **Note**: The predefined schemas offer a consistent format for specific types of content. Features like Apple Intelligence and Siri use this consistency to improve the quality of responses they offer for that type of content.

To adopt one of the predefined schemas for an app entity, type the `@AppEntity` macro before your [`AppEntity`](appentity.md) type declaration and use code completion to specify the schema you want. Add properties to your app entity to match the schema you selected. For properties that are part of the schema definition, the system infers the `@Property` macro automatically, so you don’t need to add it. For more details on how to create and implement entities, see [`Defining app entities for your custom data types`](defining-app-entities-for-your-custom-data-types.md).

##### Support Conversions Between Your App Entities and Equivalent System Types

Many apps deal with similar types of content, and might define custom app entities to represent that content. Although you can use the [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) protocol to provide alternate representations of your content, there are limitations to how other apps can use that content. The protocol supports the creation of files and binary data types, which limits what apps can do with the content. For example, Maps can’t use a picture of a landmark to generate directions to that landmark. For locations, names, and contacts, you can use the [`IntentValueRepresentation`](intentvaluerepresentation.md) type to provide a version of your data that other apps can use directly.

If your entity offers the same information found in an [`IntentPerson`](intentperson.md), [`PlaceDescriptor`](https://developer.apple.com/documentation/geotoolbox/placedescriptor), or [`PersonNameComponents`](https://developer.apple.com/documentation/foundation/personnamecomponents) type, implement the [`transferRepresentation`](https://developer.apple.com/documentation/coretransferable/transferable/transferrepresentation) property and add an [`IntentValueRepresentation`](intentvaluerepresentation.md) as one of the representations. A representation of this type supports both importing and exporting your type. The following example shows an entity that manages contact information. The code provides the contact information in an [`IntentPerson`](intentperson.md) structure so that other apps can incorporate that contact information directly.

```swift
struct ContactEntity: AppEntity, Transferable {
    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Contact"
    
    var id: String
    @Property var name: String
    @Property var email: String
    
    var displayRepresentation: DisplayRepresentation {
        .init(title: "\(name)")
    }
    
    static var defaultQuery = ContactEntityQuery()
    
    // Bidirectional conversion with IntentPerson.
    static var transferRepresentation: some TransferRepresentation {
        IntentValueRepresentation(
            exporting: { contact in
                IntentPerson(
                    identifier: .applicationDefined(contact.id),
                    name: .displayName(contact.name),
                    handle: .init(emailAddress: contact.email)
                )
            },
            importing: { person in
                guard case let .applicationDefined(id) = person.identifier?.value,
                      let handle = person.handle else {
                    throw ConversionError.missingData
                }
                return ContactEntity(
                    id: id,
                    name: person.name.displayString,
                    email: handle.value
                )
            }
        )
    }
    
    enum ConversionError: Error {
        case missingData
    }
```

For more information about making your types transferable, see the [`Core Transferable`](https://developer.apple.com/documentation/coretransferable) framework.

##### Associate Entities with the Views in Your Interface

Your app’s interface reflects the things a person is doing and what data they’re viewing or changing, but that information remains private to your app unless you tell the system about it.

To share your app’s content with the system, attach app entities to the views you use to show content:

- In SwiftUI, assign the identifier of your app entity to a view using the [`appEntityIdentifier(_:)`](https://developer.apple.com/documentation/swiftui/view/appentityidentifier(_:)) or [`appEntityUIElements(_:)`](https://developer.apple.com/documentation/swiftui/view/appentityuielements(_:)) modifier.
- In UIKit and AppKit, assign the identifier of your app entity to any responder object using the [`appEntityIdentifier`](appentityannotatable/appentityidentifier.md) property.

> ❗ **Important**: Attach app entities to views to reflect the data those views show. Don’t attach unrelated app entities to your interface.

If you don’t have a one-to-one mapping between an app entity and one of your views, add entities using the [`AppEntityUIElement`](appentityuielement.md) type. You might use this approach if your app draws all of its content in a single view or places content in [`CALayer`](https://developer.apple.com/documentation/quartzcore/calayer). With an entity UI element, you use a closure to supply the app entities for your view on demand. In SwiftUI, provide this closure using the [`appEntityUIElements(_:)`](https://developer.apple.com/documentation/swiftui/view/appentityuielements(_:)) modifier. In UIKit and AppKit, assign this closure to your view’s [`appEntityUIElementProvider`](https://developer.apple.com/documentation/uikit/uiview/appentityuielementprovider) property.

The following examples show how to use a UI element closure to specify entities for SwiftUI and UIKit views. The view in the example draws custom sticky notes, which the person can place anywhere in the view. The closure uses the system-provided context object to determine whether to return the selected notes or the notes within the specified rectangle. For each note that matches the requested criteria, it creates an [`AppEntityUIElement`](appentityuielement.md) type with the entity information and returns it to the system.

**SwiftUI**:

```swift
struct NoteBoardView: View {
    // A collection of `AppEntity` types that the view draws in its content.
    @State private var stickyNotes: [StickyNote]

    var body: some View {
        Canvas { context, size in
            stickyNotes.forEach { note in
                context.fill(
                    Path(
                        roundedRect: note.frame,
                        cornerSize: .zero
                    ),
                    with: .color(note.colorFill)
                )
            }
        }
        .appEntityUIElements { context in
            // Determine which notes, if any, require a UI element.  
            stickyNotes.compactMap { note in
                let includeNote = context.requests.contains { request in
                    switch request {
                        case .visible(let rect):
                            // Return true if the note is in the specified rectangle. 
                            return note.frame.intersects(rect)
                        case .selected:
                            // Return true if the note is selected.
                            return note.isSelected
                        @unknown default:
                            return false
                    }
                }
                // If the note isn’t visible or selected, return nil.  
                guard includeNote else {
                    return nil
                }
        
                // Return an element with the entity identifier and other details.
                return AppEntityUIElement(
                    identifier: EntityIdentifier(
                        for: StickyNote.self,
                        identifier: note.id
                    ),
                    bounds: note.frame,
                    state: State(isSelected: note.isSelected)
                )
            }
        }
    }
}
```

**UIKit**:

```swift
class NoteBoardViewController: UIViewController {
    // A collection of `AppEntity` types that the view draws in its content.
    private var stickyNotes: [StickyNote]

    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        
        self.view.appEntityUIElementProvider = { view, context in
           // Determine which notes, if any, require a UI element.  
           stickyNotes.compactMap { note in
                let includeNote = context.requests.contains { request in
                    switch request {
                        case .visible(let rect):
                            // Return true if the note is in the specified rectangle. 
                            return note.frame.intersects(rect)
                        case .selected:
                            // Return true if the note is selected.
                            return note.isSelected
                        @unknown default:
                            return false
                    }
                }
                // If the note isn’t visible or selected, return nil.  
                guard includeNote else {
                    return nil
                }
        
                // Return an element with the entity identifier and other details.
                return AppEntityUIElement(
                    identifier: EntityIdentifier(
                        for: StickyNote.self,
                        identifier: note.id
                    ),
                    bounds: note.frame,
                    state: State(isSelected: note.isSelected)
                )
            }
        }
    }
    
    // Other view controller methods and properties...
}
```

Associating app entities with your views is the best option when the current set of views reflect multiple entities. If the views reflect only one entity, add view annotations or deliver the entity using an [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) object. User activity objects store a single, optional entity in their [`appEntityIdentifier`](https://developer.apple.com/documentation/foundation/nsuseractivity/appentityidentifier) property, and the entity provides the system with similar information as an entity attached to one of your views. Delivering an entity in a user activity object is particularly relevant when your interface contains only one entity and represents an activity someone can continue on another device using Handoff. In UIKit and AppKit, assign user activity objects to views and responders using their [`userActivity`](https://developer.apple.com/documentation/uikit/uiresponder/useractivity) property. In SwiftUI, create and configure an activity object in one of your views using the [`userActivity(_:element:_:)`](https://developer.apple.com/documentation/swiftui/view/useractivity(_:element:_:)) modifier.

##### Associate Entities with Other Types of Content

If a system feature displays app-specific data, check whether you can provide an app entity with that data. Some system types support the [`AppEntityAnnotatable`](appentityannotatable.md) protocol, which gives you a way to associate an app entity with that type. For example:

- If you create local notifications with the [`User Notifications`](https://developer.apple.com/documentation/usernotifications) framework, use the [`appEntityIdentifier`](appentityannotatable/appentityidentifier.md) property of the mutable configuration object to specify an app entity with notification-related data.
- If you provide Now Playing information using the [`Media Player`](https://developer.apple.com/documentation/mediaplayer) framework, add one or more entities to the dictionary in the [`nowPlayingInfo`](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/nowplayinginfo) property of [`MPNowPlayingInfoCenter`](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter). Set the [`MPNowPlayingInfoPropertyAppEntityIdentifiers`](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyappentityidentifiers) key to the array of entities you want to associate with the current song.
- If you configure alarms using [`AlarmKit`](https://developer.apple.com/documentation/alarmkit), specify an entity along with the other alarm details when creating the [`AlarmManager.AlarmConfiguration`](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmconfiguration) type.

> **Note**: If a system type doesn’t conform to the [`AppEntityAnnotatable`](appentityannotatable.md) protocol, adding conformance to that protocol in your code doesn’t deliver any additional contextual data to the system.

## See Also

- [App schema domains](app-schema-domains.md)
  Declare support for well-known actions and content by applying system-defined schemas to your app intents, app entities, and app enumerations.
- [protocol UITableViewAppIntentsDataSource](uitableviewappintentsdatasource.md)
  The methods that an object adopts to make items in a table view discoverable by Apple Intelligence and Siri.
- [protocol NSTableViewAppIntentsDataSource](nstableviewappintentsdatasource.md)
  The methods that an object adopts to make items in a table view or outline view discoverable by Apple Intelligence and Siri.
- [protocol UICollectionViewAppIntentsDataSource](uicollectionviewappintentsdatasource.md)
  The methods adopted by the object you use to make items in a collection view discoverable by Apple Intelligence and Siri.
- [protocol NSCollectionViewAppIntentsDataSource](nscollectionviewappintentsdatasource.md)
  The methods adopted by the object you use to make items in a collection view discoverable by Apple Intelligence and Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/providing-contextual-cues-to-apple-intelligence-and-siri)*