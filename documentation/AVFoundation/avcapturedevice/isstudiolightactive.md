# isStudioLightActive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether Studio Light is active on a device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var isStudioLightActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isStudioLightActive) BOOL studioLightActive;
```

#### Discussion

When the value is [`true`](../../Swift/true.md), the system artificially lights the subject’s face to simulate the presence of a studio light near the camera.

## See Also

### Configuring Studio Light
- [class var isStudioLightEnabled: Bool](./isstudiolightenabled.md)
  A Boolean value that indicates whether a user enabled Studio Light on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isstudiolightactive)*