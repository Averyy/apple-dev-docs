# CardSnippet

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A type that presents the SwiftUI view for an app entity as a card.

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
struct CardSnippet<Entity, Content> where Entity : AppEntity, Content : View
```

## Overview

A `CardSnippet` type generates a card-style presentation that includes the contents of a SwiftUI view you provide. The system delivers cards in various contexts, including Siri responses and conversation transcripts. When your entity adopts the [`SnippetRepresentableEntity`](./snippetrepresentableentity.md) protocol, you create this type and return it from your entity’s [`snippet`](./snippetrepresentableentity/snippet.md) property.

When you create a `CardSnippet`, you provide a view builder that returns a SwiftUI view with content from the specified entity. The system creates a SwiftUI view archive from it to display your view in different contexts. You specify which contexts you support at initialization time by specifying the families you support. If your snippet doesn’t support a requested family, the system shows the content from your entity’s display representation instead of the archived view.

The following example shows the creation of a `CardSnippet` for an entity that manages a photo. The snippet supports the standard family, which offers sufficient space to display your content on iPhone or similarly large display. When the system runs the provided closure, it provides you with the entity to display
and a context object for adjusting the configuration of your views.

```swift
extension PhotoEntity: SnippetRepresentableEntity {
    static var snippet: some EntitySnippetContent<Self> {
        CardSnippet(supportedFamilies: [.standard]) { photo, context in
            PhotoCardView(photo: photo)
        }
    }
}
```

When you build the content for your snippet, create views with primarily static content such as text and images. The system renders snippets in advance and stores your views in a static archive it can use at any time, including when your app isn’t running. Because rendering happens in advance, you can’t change the content of your view dynamically later. If your view requires data that isn’t immediately available in your entity, prepare the data before returning the SwiftUI view from your snippet. For example, if you need to create custom images, create them before you return your view. Prepare data synchronously to ensure it’s available when you create your view. If you generate data asynchronously, it likely won’t be available in time.

## Topics

### Creating a card snippet
- [init(supportedFamilies: [CardSnippetFamily], content: (Entity, CardSnippetContext) -> Content)](./cardsnippet/init%28supportedfamilies,content%29.md)
  Creates a card snippet with the views for specific families of content.

## Relationships

### Conforms To
- [EntitySnippetContent](./entitysnippetcontent.md)

## See Also

### Card snippets
- [protocol SnippetRepresentableEntity](./snippetrepresentableentity.md)
  An app entity that provides a visual representation for its content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/cardsnippet)*