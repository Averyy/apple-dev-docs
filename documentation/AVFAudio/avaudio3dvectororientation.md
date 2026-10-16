# AVAudio3DVectorOrientation

**Framework**: AVFAudio  
**Kind**: struct

A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.

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
struct AVAudio3DVectorOrientation
```

#### Overview

Two orthogonal vectors describe the orientation of the listener. The forward vector points in the direction the listener faces. The up vector is orthogonal to the forward vector and points upward from the listener’s head.

## Topics

### Creating a vector orientation
- [init()](avaudio3dvectororientation/init.md)
  Creates a 3D vector orientation instance.
- [init(forward: AVAudio3DVector, up: AVAudio3DVector)](avaudio3dvectororientation/init(forward:up:).md)
  Creates a 3D vector orientation instance using the forward and up vectors you specify.
- [func AVAudioMake3DVectorOrientation(AVAudio3DVector, AVAudio3DVector) -> AVAudio3DVectorOrientation](avaudiomake3dvectororientation(_:_:).md)
  Creates a 3D vector orientation instance using the forward and up vectors you specify.
### Getting vector orientation properties
- [var forward: AVAudio3DVector](avaudio3dvectororientation/forward.md)
  The forward vector points in the direction that the listener faces.
- [var up: AVAudio3DVector](avaudio3dvectororientation/up.md)
  The up vector is orthogonal to the forward vector and points upward from the listener’s head.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [struct AVAudio3DPoint](avaudio3dpoint.md)
  A structure that represents a point in 3D space.
- [typealias AVAudio3DVector](avaudio3dvector.md)
  A structure that represents a vector in 3D space, in degrees.
- [struct AVAudio3DAngularOrientation](avaudio3dangularorientation.md)
  A structure that represents the angular orientation of the listener in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dvectororientation)*