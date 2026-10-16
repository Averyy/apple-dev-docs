# AVAudio3DVector

**Framework**: AVFAudio  
**Kind**: typealias

A structure that represents a vector in 3D space, in degrees.

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
typealias AVAudio3DVector = AVAudio3DPoint
```

#### Discussion

Classes that deal with 3D audio use this structure, such as those that adopt the [`AVAudioMixing`](avaudiomixing.md) protocol and the [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) class.

## Topics

### Vector creation
- [func AVAudioMake3DVector(Float, Float, Float) -> AVAudio3DVector](avaudiomake3dvector(_:_:_:).md)
  Creates a vector in 3D space, in degrees.

## See Also

- [struct AVAudio3DPoint](avaudio3dpoint.md)
  A structure that represents a point in 3D space.
- [struct AVAudio3DVectorOrientation](avaudio3dvectororientation.md)
  A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.
- [struct AVAudio3DAngularOrientation](avaudio3dangularorientation.md)
  A structure that represents the angular orientation of the listener in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dvector)*