# EntitySnippetContentBuilder

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

A result builder that assembles an entity’s snippet declarations.

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
@resultBuilder
enum EntitySnippetContentBuilder<Entity> where Entity : AppEntity
```

## Overview

The builder backs the [`snippet`](./snippetrepresentableentity/snippet.md) property of a [`SnippetRepresentableEntity`](./snippetrepresentableentity.md) type. For example, providing a [`CardSnippet`](./cardsnippet.md) instance to the `snippet` property implicitly applies this builder for that type.

## Topics

### Type Methods
- [static func buildBlock<C>(C) -> some EntitySnippetContent<Entity>
](./entitysnippetcontentbuilder/buildblock%28_%29.md)
  Creates a snippet from a single view declaration.
- [static func buildBlock<C1, C2>(C1, C2) -> some EntitySnippetContent<Entity>
](./entitysnippetcontentbuilder/buildblock%28_,_%29.md)
  Creates a snippet by combining two snippet declarations into a single representation.
- [static func buildExpression(some EntitySnippetContent<Entity>) -> some EntitySnippetContent<Entity>
](./entitysnippetcontentbuilder/buildexpression%28_%29.md)

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
- [struct CardSnippetSize](./cardsnippetsize.md)
  A size category for a snippet card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitysnippetcontentbuilder)*