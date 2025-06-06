# AVAudioMake3DAngularOrientation(_:_:_:)

**Framework**: AVFAudio  
**Kind**: func

Creates a 3D angular orientation using the yaw, pitch, and roll values you specify.

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
func AVAudioMake3DAngularOrientation(_ yaw: Float, _ pitch: Float, _ roll: Float) -> AVAudio3DAngularOrientation
```

#### Return Value

A new [`AVAudio3DAngularOrientation`](avaudio3dangularorientation.md) instance.

## Parameters

- `yaw`: The side-to-side movement of the listener’s head.
- `pitch`: The up-and-down movement of the listener’s head.
- `roll`: The tilt of the listener’s head.

## See Also

- [init()](avaudio3dangularorientation/init.md)
  Creates an angular orientation.
- [init(yaw: Float, pitch: Float, roll: Float)](avaudio3dangularorientation/init(yaw:pitch:roll:).md)
  Creates a 3D angular orientation using the yaw, pitch, and roll values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiomake3dangularorientation(_:_:_:))*