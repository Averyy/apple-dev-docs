# yaw

**Framework**: AVFAudio  
**Kind**: property

The side-to-side movement of the listener’s head.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var yaw: Float
```

#### Discussion

The yaw axis describes the side-to-side movement of the listener’s head, and is perpendicular to the plane of the listener’s ears. Its origin is at the center of the listener’s head and points toward the bottom of the head. A positive yaw is in the clockwise direction going from `0` to `180` degrees. A negative yaw is in the counterclockwise direction going from `0` to `-180` degrees.

## See Also

- [var pitch: Float](avaudio3dangularorientation/pitch.md)
  The up-and-down movement of the listener’s head.
- [var roll: Float](avaudio3dangularorientation/roll.md)
  The tilt of the listener’s head.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dangularorientation/yaw)*