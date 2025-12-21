# isCameraSensorOrientationCompensationEnabled

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var isCameraSensorOrientationCompensationEnabled: Bool { get set }
```

#### Discussion

A BOOL value indicating that still image buffers will be rotated to match the sensor orientation of earlier generation hardware.

Default is YES when cameraSensorOrientationCompensationSupported is YES. Set to NO if your app does not require sensor orientation compensation.

## See Also

- [var isCameraSensorOrientationCompensationSupported: Bool](avcapturestillimageoutput/iscamerasensororientationcompensationsupported.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/iscamerasensororientationcompensationenabled)*