# init(_:duration:startVelocity:endVelocity:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new keyframe using the given value and timestamp.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(_ to: Value, duration: TimeInterval, startVelocity: Value? = nil, endVelocity: Value? = nil)
```

## Parameters

- `to`: The value of the keyframe.
- `duration`: The duration of the segment defined by this keyframe.
- `startVelocity`: The velocity of the value at the beginning of the   segment, or   to automatically compute the velocity to maintain   smooth motion.
- `endVelocity`: The velocity of the value at the end of the segment,   or   to automatically compute the velocity to maintain smooth   motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/cubickeyframe/init(_:duration:startvelocity:endvelocity:))*