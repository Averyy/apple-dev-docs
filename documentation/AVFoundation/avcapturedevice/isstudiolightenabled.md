# isStudioLightEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether a user enabled Studio Light on a device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
class var isStudioLightEnabled: Bool { get }
```

```objc
@property (class, readonly, getter=isStudioLightEnabled) BOOL studioLightEnabled;
```

#### Discussion

When the value is [`true`](../../Swift/true.md), the system artificially lights the subject’s face to simulate the presence of a studio light near the camera.

This property is key-value observable.

## See Also

### Configuring Studio Light
- [var isStudioLightActive: Bool](./isstudiolightactive.md)
  A Boolean value that indicates whether Studio Light is active on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isstudiolightenabled)*