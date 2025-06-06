# listenerAngularOrientation

**Framework**: AVFAudio  
**Kind**: property

The listener’s angular orientation in the environment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var listenerAngularOrientation: AVAudio3DAngularOrientation { get set }
```

#### Discussion

The system specifies all angles in degrees.

The default orientation is with the listener looking directly along the negative z-axis (forward). This orientation has a yaw of `0.0` degrees, a pitch of `0.0` degrees, and a roll of `0.0` degrees.

Changing this property results in a corresponding change in the [`listenerVectorOrientation`](avaudioenvironmentnode/listenervectororientation.md) property.

## See Also

- [var listenerPosition: AVAudio3DPoint](avaudioenvironmentnode/listenerposition.md)
  The listener’s position in the 3D environment.
- [var listenerVectorOrientation: AVAudio3DVectorOrientation](avaudioenvironmentnode/listenervectororientation.md)
  The listener’s vector orientation in the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentnode/listenerangularorientation)*