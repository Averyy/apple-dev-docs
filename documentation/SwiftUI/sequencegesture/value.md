# SequenceGesture.Value

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

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
- [SequenceGesture.Value.first(_:)](./value/first%28_%29.md)
  The first gesture hasn’t ended.
- [case second(First.Value, Second.Value?)](./value/second%28_,_%29.md)
  The first gesture has ended.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sequencegesture/value)*