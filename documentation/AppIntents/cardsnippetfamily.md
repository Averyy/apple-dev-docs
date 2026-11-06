# CardSnippetFamily

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A type that defines the supported rendering environments for card snippets.

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
struct CardSnippetFamily
```

## Overview

Each instance of the `CardSnippetFamily` type reflects the amount of space available for your custom content, and indicates how the system intends to display that content. When defining a [`CardSnippet`](./cardsnippet.md) type for one of your entities, you specify which families you support. In the closure you use to create your view, the system provides a [`CardSnippetContext`](./cardsnippetcontext.md) object with the family it expects you to use to configure your views.

The system defines families broadly so that it can reuse your snippets in multiple places. For example, the [`standard`](./cardsnippetfamily/standard.md) family supports a view large enough to display on iPad or iPhone. If an entity doesn’t support the requested family, the system presents the entity’s display representation details instead.

## Topics

### Getting the supported families
- [static var standard: CardSnippetFamily](./cardsnippetfamily/standard.md)
  A family that supports a standard amount of space.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Card snippets
- [protocol SnippetRepresentableEntity](./snippetrepresentableentity.md)
  An app entity that provides a visual representation for its content.
- [struct CardSnippet](./cardsnippet.md)
  A type that presents the SwiftUI view for an app entity as a card.
- [struct CardSnippetContext](./cardsnippetcontext.md)
  A type that stores information about how to render a card snippet.
- [protocol EntitySnippetContent](./entitysnippetcontent.md)
  A visual representation that the system renders for an entity.
- [enum EntitySnippetContentBuilder](./entitysnippetcontentbuilder.md)
  A result builder that assembles an entity’s snippet declarations.
- [struct CardSnippetSize](./cardsnippetsize.md)
  A size category for a snippet card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/cardsnippetfamily)*