# Text.WritingDirectionStrategy

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The way SwiftUI infers the appropriate writing direction if no value is explicitly provided.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct WritingDirectionStrategy
```

## Topics

### Type Properties
- [static let contentBased: Text.WritingDirectionStrategy](./writingdirectionstrategy/contentbased.md)
  The writing direction following the language of the string that is laid out.
- [static let `default`: Text.WritingDirectionStrategy](./writingdirectionstrategy/default.md)
  The default strategy is [`contentBased`](./writingdirectionstrategy/contentbased.md).
- [static let layoutBased: Text.WritingDirectionStrategy](./writingdirectionstrategy/layoutbased.md)
  The writing direction following the general UI layout direction.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/writingdirectionstrategy)*