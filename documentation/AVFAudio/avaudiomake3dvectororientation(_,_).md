# AVAudioMake3DVectorOrientation(_:_:)

**Framework**: AVFAudio  
**Kind**: func  
**Role**: Function

Creates a 3D vector orientation instance using the forward and up vectors you specify.

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
func AVAudioMake3DVectorOrientation(_ forward: AVAudio3DVector, _ up: AVAudio3DVector) -> AVAudio3DVectorOrientation
```

```c
static AVAudio3DVectorOrientation AVAudioMake3DVectorOrientation(AVAudio3DVector forward, AVAudio3DVector up);
```

#### Return Value

A new [`AVAudioMake3DVectorOrientation(_:_:)`](./avaudiomake3dvectororientation%28_,_%29.md) object.

## Parameters

- `forward`: The forward vector points in the direction that the listener faces.
- `up`: The up vector is orthogonal to the forward vector and points upward from the listener’s head.

## See Also

### Creating a vector orientation
- [init()](./avaudio3dvectororientation/init%28%29.md)
  Creates a 3D vector orientation instance.
- [init(forward: AVAudio3DVector, up: AVAudio3DVector)](./avaudio3dvectororientation/init%28forward,up%29.md)
  Creates a 3D vector orientation instance using the forward and up vectors you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiomake3dvectororientation(_:_:))*