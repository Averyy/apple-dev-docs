# EntitySnippetContent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

A visual representation that the system renders for an entity.

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
protocol EntitySnippetContent<Entity>
```

## Overview

You don’t conform to this protocol directly. Instead, you build an entity’s presentation from a type that already conforms to it, such as [`CardSnippet`](./cardsnippet.md), and return it from the [`snippet`](./snippetrepresentableentity/snippet-swift.type.property.md) property of a [`SnippetRepresentableEntity`](./snippetrepresentableentity.md) type.

## Topics

### Associated Types
- [associatedtype Entity : AppEntity](./entitysnippetcontent/entity.md)
  An entity type that the snippet content represents.
### Instance Methods
- [func contentMarginsDisabled(Bool) -> some EntitySnippetContent<Self.Entity>
](./entitysnippetcontent/contentmarginsdisabled%28_%29.md)
  Disables the default content margins.
### Type Aliases
- [EntitySnippetContent.Input](./entitysnippetcontent/input.md)
- [EntitySnippetContent.Output](./entitysnippetcontent/output.md)

## Relationships

### Conforming Types
- [CardSnippet](./cardsnippet.md)

## See Also

### Card snippets
- [Presenting an entity as a card snippet](./presenting-an-entity-as-a-card-snippet.md)
  Show a custom view of your app’s content in system experiences such as Siri responses and conversation transcripts.
- [protocol SnippetRepresentableEntity](./snippetrepresentableentity.md)
  An app entity that provides a visual representation for its content.
- [struct CardSnippet](./cardsnippet.md)
  A type that presents the SwiftUI view for an app entity as a card.
- [struct CardSnippetContext](./cardsnippetcontext.md)
  A type that stores information about how to render a card snippet.
- [struct CardSnippetFamily](./cardsnippetfamily.md)
  A type that defines the supported rendering environments for card snippets.
- [enum EntitySnippetContentBuilder](./entitysnippetcontentbuilder.md)
  A result builder that assembles an entity’s snippet declarations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitysnippetcontent)*