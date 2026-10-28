# AVAudioMake3DAngularOrientation(_:_:_:)

**Framework**: AVFAudio  
**Kind**: func  
**Role**: Function

Creates a 3D angular orientation using the yaw, pitch, and roll values you specify.

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
func AVAudioMake3DAngularOrientation(_ yaw: Float, _ pitch: Float, _ roll: Float) -> AVAudio3DAngularOrientation
```

```c
static AVAudio3DAngularOrientation AVAudioMake3DAngularOrientation(float yaw, float pitch, float roll);
```

## Return Value

A new [`AVAudio3DAngularOrientation`](./avaudio3dangularorientation.md) instance.

## Parameters

- `yaw`: The side-to-side movement of the listener’s head.
- `pitch`: The up-and-down movement of the listener’s head.
- `roll`: The tilt of the listener’s head.

## See Also

### Creating an angular orientation
- [init()](./avaudio3dangularorientation/init%28%29.md)
  Creates an angular orientation.
- [init(yaw: Float, pitch: Float, roll: Float)](./avaudio3dangularorientation/init%28yaw,pitch,roll%29.md)
  Creates a 3D angular orientation using the yaw, pitch, and roll values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiomake3dangularorientation(_:_:_:))*