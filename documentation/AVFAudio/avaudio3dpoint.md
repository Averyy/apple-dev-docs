# AVAudio3DPoint

**Framework**: AVFAudio  
**Kind**: struct

A structure that represents a point in 3D space.

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
struct AVAudio3DPoint
```

#### Overview

Classes that deal with 3D audio, such as those adopting [`AVAudioMixing`](avaudiomixing.md) and [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md), use this structure. The system represents this point in meters.

## Topics

### Creating a point
- [init()](avaudio3dpoint/init.md)
  Creates a 3D point.
- [init(x: Float, y: Float, z: Float)](avaudio3dpoint/init(x:y:z:).md)
  Creates a 3D point using the x, y, and z coordinates you specify.
- [func AVAudioMake3DPoint(Float, Float, Float) -> AVAudio3DPoint](avaudiomake3dpoint(_:_:_:).md)
  Creates a 3D point using the x, y, and z coordinates you specify.
### Getting point properties
- [var x: Float](avaudio3dpoint/x.md)
  The location on the x-axis, in meters.
- [var y: Float](avaudio3dpoint/y.md)
  The location on the y-axis, in meters.
- [var z: Float](avaudio3dpoint/z.md)
  The location on the z-axis, in meters.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [typealias AVAudio3DVector](avaudio3dvector.md)
  A structure that represents a vector in 3D space, in degrees.
- [struct AVAudio3DVectorOrientation](avaudio3dvectororientation.md)
  A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.
- [struct AVAudio3DAngularOrientation](avaudio3dangularorientation.md)
  A structure that represents the angular orientation of the listener in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dpoint)*