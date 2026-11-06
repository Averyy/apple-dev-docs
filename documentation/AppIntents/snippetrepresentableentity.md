# SnippetRepresentableEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

An app entity that provides a visual representation for its content.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
protocol SnippetRepresentableEntity : AppEntity
```

## Overview

Adopt the `SnippetRepresentableEntity` protocol in your app entity when you want to provide a visual representation of its content. This protocol conforms to the base [`AppEntity`](./appentity.md) protocol and adds a [`snippet`](./snippetrepresentableentity/snippet.md) property for delivering a snippet type to display your entity’s content. When the system needs to show information about your entity, it displays the contents of your snippet. For example, Siri might show the snippet during a conversation to confirm a choice or display details about a requested item.

Implement the [`snippet`](./snippetrepresentableentity/snippet.md) property in your entity type and return a snippet with the SwiftUI view you want the system to display. In the following example, the property returns a [`CardSnippet`](./cardsnippet.md) type, which delivers the custom `MessageSnipperCard` view from the app. This view uses the provided message object to configure the views it displays.

```swift
extension MessageEntity: SnippetRepresentableEntity {
    static var snippet: some EntitySnippetContent<MessageEntity> {
        CardSnippet(supportedFamilies: [.standard]) { message, _ in
            // Prepare any extra data before returning the view.
            MessageSnippetCard(message: message)
        }
    }
}
```

When you build the content for your snippet, create views with primarily static content such as text and images. The system renders snippets in advance and stores your views in a static archive it can use at any time, including when your app isn’t running. Because rendering happens in advance, you can’t change the content of your view dynamically later. If your view requires data that isn’t immediately available in your entity, prepare the data before returning the SwiftUI view from your snippet. For example, if you need to create custom images, create them before you return your view. Prepare data synchronously to ensure it’s available when you create your view. If you generate data asynchronously, it likely won’t be available in time.

To include interactive controls in your view, add a SwiftUI control that runs an app intent. For example, you can initialize a [`Button`](../SwiftUI/button.md) or [`Toggle`](../SwiftUI/toggle.md) view with an app intent. When someone interacts with one of your controls, the system runs the specified app intent. After your app intent runs, the system generates a new SwiftUI view archive for your snippet, incorporating any changes you made to your views because of the app intent.

## Topics

### Configuring the snippet
- [static var snippet: Self.Body](./snippetrepresentableentity/snippet.md)
  The snippet that contains the view to display.
- [associatedtype Body : EntitySnippetContent](./snippetrepresentableentity/body.md)

## Relationships

### Inherits From
- [AppEntity](./appentity.md)
- [AppValue](./appvalue.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/customlocalizedstringresourceconvertible.md)
- [DisplayRepresentable](./displayrepresentable.md)
- [Identifiable](../Swift/identifiable.md)
- [InstanceDisplayRepresentable](./instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](./persistentlyidentifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TypeDisplayRepresentable](./typedisplayrepresentable.md)

## See Also

### Card snippets
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
- [struct CardSnippetSize](./cardsnippetsize.md)
  A size category for a snippet card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/snippetrepresentableentity)*