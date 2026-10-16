# AVAudio3DAngularOrientation

**Framework**: AVFAudio  
**Kind**: struct

A structure that represents the angular orientation of the listener in 3D space.

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
struct AVAudio3DAngularOrientation
```

#### Overview

This represents the three angles that describe the orientation of a listener’s head — yaw, pitch, and roll.

## Topics

### Creating an angular orientation
- [init()](avaudio3dangularorientation/init.md)
  Creates an angular orientation.
- [init(yaw: Float, pitch: Float, roll: Float)](avaudio3dangularorientation/init(yaw:pitch:roll:).md)
  Creates a 3D angular orientation using the yaw, pitch, and roll values you specify.
- [func AVAudioMake3DAngularOrientation(Float, Float, Float) -> AVAudio3DAngularOrientation](avaudiomake3dangularorientation(_:_:_:).md)
  Creates a 3D angular orientation using the yaw, pitch, and roll values you specify.
### Getting angular orientation properties
- [var yaw: Float](avaudio3dangularorientation/yaw.md)
  The side-to-side movement of the listener’s head.
- [var pitch: Float](avaudio3dangularorientation/pitch.md)
  The up-and-down movement of the listener’s head.
- [var roll: Float](avaudio3dangularorientation/roll.md)
  The tilt of the listener’s head.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [struct AVAudio3DPoint](avaudio3dpoint.md)
  A structure that represents a point in 3D space.
- [typealias AVAudio3DVector](avaudio3dvector.md)
  A structure that represents a vector in 3D space, in degrees.
- [struct AVAudio3DVectorOrientation](avaudio3dvectororientation.md)
  A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dangularorientation)*