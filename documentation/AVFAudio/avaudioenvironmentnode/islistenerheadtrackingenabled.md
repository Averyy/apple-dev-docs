# isListenerHeadTrackingEnabled

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the listener orientation is automatically rotated based on head orientation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isListenerHeadTrackingEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isListenerHeadTrackingEnabled) BOOL listenerHeadTrackingEnabled;
```

#### Discussion

To enable head tracking, your app must have the [`com.apple.developer.coremotion.head-pose`](../../BundleResources/entitlements/com.apple.developer.coremotion.head-pose.md) entitlement.

Set this value to [`true`](../../Swift/true.md) to enable head tracking with compatible AirPods.

## See Also

### Positioning the listener
- [var listenerPosition: AVAudio3DPoint](./listenerposition.md)
  The listener’s position in the 3D environment.
- [var listenerAngularOrientation: AVAudio3DAngularOrientation](./listenerangularorientation.md)
  The listener’s angular orientation in the environment.
- [var listenerVectorOrientation: AVAudio3DVectorOrientation](./listenervectororientation.md)
  The listener’s vector orientation in the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentnode/islistenerheadtrackingenabled)*