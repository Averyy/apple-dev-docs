# listenerPosition

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The listener’s position in the 3D environment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var listenerPosition: AVAudio3DPoint { get set }
```

```objc
@property (nonatomic) AVAudio3DPoint listenerPosition;
```

## Discussion

The system specifies the coordinates in meters.

## See Also

### Positioning the listener
- [var listenerAngularOrientation: AVAudio3DAngularOrientation](./listenerangularorientation.md)
  The listener’s angular orientation in the environment.
- [var listenerVectorOrientation: AVAudio3DVectorOrientation](./listenervectororientation.md)
  The listener’s vector orientation in the environment.
- [var isListenerHeadTrackingEnabled: Bool](./islistenerheadtrackingenabled.md)
  A Boolean value that indicates whether the listener orientation is automatically rotated based on head orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentnode/listenerposition)*