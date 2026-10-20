# yaw

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The side-to-side movement of the listener’s head.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var yaw: Float
```

```c
float yaw;
```

#### Discussion

The yaw axis describes the side-to-side movement of the listener’s head, and is perpendicular to the plane of the listener’s ears. Its origin is at the center of the listener’s head and points toward the bottom of the head. A positive yaw is in the clockwise direction going from `0` to `180` degrees. A negative yaw is in the counterclockwise direction going from `0` to `-180` degrees.

## See Also

### Getting angular orientation properties
- [var pitch: Float](./pitch.md)
  The up-and-down movement of the listener’s head.
- [var roll: Float](./roll.md)
  The tilt of the listener’s head.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dangularorientation/yaw)*