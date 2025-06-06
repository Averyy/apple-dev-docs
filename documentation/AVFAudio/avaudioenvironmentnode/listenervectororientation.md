# listenerVectorOrientation

**Framework**: AVFAudio  
**Kind**: property

The listener’s vector orientation in the environment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var listenerVectorOrientation: AVAudio3DVectorOrientation { get set }
```

#### Discussion

The default orientation is with the listener looking directly along the negative z-axis (forward).

The node expresses a forward vector orientation as `(0, 0, -1)`, and an up vector as `(0, 1, 0)`.

Changing this property results in a corresponding change in the [`listenerAngularOrientation`](avaudioenvironmentnode/listenerangularorientation.md) property.

## See Also

- [var listenerPosition: AVAudio3DPoint](avaudioenvironmentnode/listenerposition.md)
  The listener’s position in the 3D environment.
- [var listenerAngularOrientation: AVAudio3DAngularOrientation](avaudioenvironmentnode/listenerangularorientation.md)
  The listener’s angular orientation in the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentnode/listenervectororientation)*