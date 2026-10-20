# isCameraSensorOrientationCompensationEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 26.0+ - Deprecated in 10.0
- iPadOS 26.0+ - Deprecated in 10.0
- Mac Catalyst 26.0+ - Deprecated in 10.0

## Declaration

```swift
var isCameraSensorOrientationCompensationEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isCameraSensorOrientationCompensationEnabled) BOOL cameraSensorOrientationCompensationEnabled;
```

#### Discussion

A BOOL value indicating that still image buffers will be rotated to match the sensor orientation of earlier generation hardware.

Default is YES when cameraSensorOrientationCompensationSupported is YES. Set to NO if your app does not require sensor orientation compensation.

## See Also

### Configuring orientation compensation
- [var isCameraSensorOrientationCompensationSupported: Bool](./iscamerasensororientationcompensationsupported.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/iscamerasensororientationcompensationenabled)*