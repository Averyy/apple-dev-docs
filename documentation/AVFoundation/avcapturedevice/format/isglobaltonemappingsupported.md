# isGlobalToneMappingSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the format supports global tone mapping.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isGlobalToneMappingSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isGlobalToneMappingSupported) BOOL globalToneMappingSupported;
```

## See Also

### Determining color support
- [var supportedColorSpaces: [AVCaptureColorSpace]](./supportedcolorspaces.md)
  The list of the device’s supported color spaces.
- [supportedColorSpaces](../../avcapturedeviceformat/supportedcolorspaces.md)
  The list of color spaces the format supports for image and video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isglobaltonemappingsupported)*