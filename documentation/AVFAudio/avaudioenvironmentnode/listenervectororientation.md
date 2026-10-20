# listenerVectorOrientation

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) AVAudio3DVectorOrientation listenerVectorOrientation;
```

#### Discussion

The default orientation is with the listener looking directly along the negative z-axis (forward).

The node expresses a forward vector orientation as `(0, 0, -1)`, and an up vector as `(0, 1, 0)`.

Changing this property results in a corresponding change in the [`listenerAngularOrientation`](./listenerangularorientation.md) property.

## See Also

### Positioning the listener
- [var listenerPosition: AVAudio3DPoint](./listenerposition.md)
  The listener’s position in the 3D environment.
- [var listenerAngularOrientation: AVAudio3DAngularOrientation](./listenerangularorientation.md)
  The listener’s angular orientation in the environment.
- [var isListenerHeadTrackingEnabled: Bool](./islistenerheadtrackingenabled.md)
  A Boolean value that indicates whether the listener orientation is automatically rotated based on head orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentnode/listenervectororientation)*