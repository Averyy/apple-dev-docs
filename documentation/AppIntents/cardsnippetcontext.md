# CardSnippetContext

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A type that stores information about how to render a card snippet.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct CardSnippetContext
```

## Overview

The `CardSnippetContext` type stores information that you use to render the views of a card snippet. When you create a `CardSnippet` for your entity, you specify a closure that accepts an instance of this type as a parameter. When the system needs to render a specific instance of your entity type, it passes the entity and a `CardSnippetContext` object to your closure. The context object contains information about the rendering environment, and you use this information to adjust your view-creation code.

The `CardSnippetContext` type contains only information that’s specific to card snippets. During rendering, use SwiftUI environment values to adjust your rendering code. For example, you might retrieve the current color scheme and locale from the [`colorScheme`](../SwiftUI/environmentvalues/colorscheme.md) and [`locale`](../SwiftUI/environmentvalues/locale.md) environment values. For more information about how to use SwiftUI environment values, see [`EnvironmentValues`](../SwiftUI/environmentvalues.md).

## Topics

### Getting the environment details
- [var family: CardSnippetFamily](./cardsnippetcontext/family.md)
  The environment with which to configure your views.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Card snippets
- [protocol SnippetRepresentableEntity](./snippetrepresentableentity.md)
  An app entity that provides a visual representation for its content.
- [struct CardSnippet](./cardsnippet.md)
  A type that presents the SwiftUI view for an app entity as a card.
- [struct CardSnippetFamily](./cardsnippetfamily.md)
  A type that defines the supported rendering environments for card snippets.
- [protocol EntitySnippetContent](./entitysnippetcontent.md)
  A visual representation that the system renders for an entity.
- [enum EntitySnippetContentBuilder](./entitysnippetcontentbuilder.md)
  A result builder that assembles an entity’s snippet declarations.
- [struct CardSnippetSize](./cardsnippetsize.md)
  A size category for a snippet card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/cardsnippetcontext)*