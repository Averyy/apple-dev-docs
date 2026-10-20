# init(_:_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a gesture with two gestures that can receive updates or succeed independently of each other.

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
nonisolated
init(_ first: First, _ second: Second)
```

## Parameters

- `first`: The first of two gestures that can happen simultaneously.
- `second`: The second of two gestures that can happen simultaneously.

## See Also

### Creating the gesture
- [var first: First](./first.md)
  The first of two gestures that can happen simultaneously.
- [var second: Second](./second.md)
  The second of two gestures that can happen simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/simultaneousgesture/init(_:_:))*