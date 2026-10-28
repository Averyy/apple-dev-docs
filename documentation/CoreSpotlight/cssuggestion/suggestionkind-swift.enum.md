# CSSuggestion.SuggestionKind

**Framework**: Core Spotlight  
**Kind**: enum  
**Role**: Enumeration

The suggestion type that determines how the system handles a suggestion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum SuggestionKind
```

```c
enum CSSuggestionKind : NSInteger;
```

## Overview

Suggestions that the system returns from the query handler have [`CSSuggestion.SuggestionKind.default`](./suggestionkind-swift.enum/default.md).

## Topics

### Suggestion types
- [CSSuggestion.SuggestionKind.none](./suggestionkind-swift.enum/none.md)
  Blocks the system from displaying the suggestion.
- [CSSuggestion.SuggestionKind.custom](./suggestionkind-swift.enum/custom.md)
  Sorts the custom suggestions together.
- [CSSuggestion.SuggestionKind.default](./suggestionkind-swift.enum/default.md)
  Displays the suggestion normally.
### Initializers
- [init?(rawValue: Int)](./suggestionkind-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting suggestion attributes
- [var localizedAttributedSuggestion: AttributedString](./localizedattributedsuggestion-3ssly.md)
  An attributed string for the localized suggestion.
- [var suggestionKind: CSSuggestion.SuggestionKind](./suggestionkind-swift.property.md)
  The type of suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssuggestion/suggestionkind-swift.enum)*