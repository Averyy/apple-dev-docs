# SequenceGesture.Value

**Framework**: SwiftUI  
**Kind**: enum

The value of a sequence gesture that helps to detect whether the first gesture succeeded, so the second gesture can start.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
enum Value
```

## Topics

### Getting gesture values
- [SequenceGesture.Value.first(_:)](sequencegesture/value/first(_:).md)
  The first gesture hasn’t ended.
- [case second(First.Value, Second.Value?)](sequencegesture/value/second(_:_:).md)
  The first gesture has ended.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sequencegesture/value)*