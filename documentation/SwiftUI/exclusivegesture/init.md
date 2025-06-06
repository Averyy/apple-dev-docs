# init(_:_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a gesture from two gestures where only one of them succeeds.

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
init(_ first: First, _ second: Second)
```

## Parameters

- `first`: The first of two gestures. This gesture has precedence over   the other gesture.
- `second`: The second of two gestures.

## See Also

- [var first: First](exclusivegesture/first.md)
  The first of two gestures.
- [var second: Second](exclusivegesture/second.md)
  The second of two gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/exclusivegesture/init(_:_:))*