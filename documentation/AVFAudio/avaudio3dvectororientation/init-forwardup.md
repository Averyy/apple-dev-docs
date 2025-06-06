# init(forward:up:)

**Framework**: AVFAudio  
**Kind**: init

Creates a 3D vector orientation instance using the forward and up vectors you specify.

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
init(forward: AVAudio3DVector, up: AVAudio3DVector)
```

## Parameters

- `forward`: The forward vector points in the direction that the listener faces.
- `up`: The up vector is orthogonal to the forward vector and points upward from the listener’s head.

## See Also

- [init()](avaudio3dvectororientation/init.md)
  Creates a 3D vector orientation instance.
- [func AVAudioMake3DVectorOrientation(AVAudio3DVector, AVAudio3DVector) -> AVAudio3DVectorOrientation](avaudiomake3dvectororientation(_:_:).md)
  Creates a 3D vector orientation instance using the forward and up vectors you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dvectororientation/init(forward:up:))*