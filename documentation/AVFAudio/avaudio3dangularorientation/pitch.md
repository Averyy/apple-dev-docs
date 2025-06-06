# pitch

**Framework**: AVFAudio  
**Kind**: property

The up-and-down movement of the listener’s head.

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
var pitch: Float
```

#### Discussion

The pitch axis describes the up-and-down movement of the listener’s head, and is perpendicular to the yaw axis. It’s parallel to the plane of the listener’s ears. Its origin is at the center of the listener’s head and points toward the right ear. A positive pitch is the upward direction going from `0` to `180` degrees. A negative pitch is in the downward direction going from `0` to `-180` degrees.

## See Also

- [var yaw: Float](avaudio3dangularorientation/yaw.md)
  The side-to-side movement of the listener’s head.
- [var roll: Float](avaudio3dangularorientation/roll.md)
  The tilt of the listener’s head.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dangularorientation/pitch)*