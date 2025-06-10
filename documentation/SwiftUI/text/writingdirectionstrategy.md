# Text.WritingDirectionStrategy

**Framework**: SwiftUI  
**Kind**: struct

The way SwiftUI infers the appropriate writing direction if no value is explicitly provided.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct WritingDirectionStrategy
```

## Topics

### Type Properties
- [static let contentBased: Text.WritingDirectionStrategy](text/writingdirectionstrategy/contentbased.md)
  The writing direction following the language of the string that is laid out.
- [static let `default`: Text.WritingDirectionStrategy](text/writingdirectionstrategy/default.md)
  The default strategy is [`contentBased`](text/writingdirectionstrategy/contentbased.md).
- [static let layoutBased: Text.WritingDirectionStrategy](text/writingdirectionstrategy/layoutbased.md)
  The writing direction following the general UI layout direction.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/writingdirectionstrategy)*