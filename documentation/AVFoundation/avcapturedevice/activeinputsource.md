# activeInputSource

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The currently active input source of the device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var activeInputSource: AVCaptureDevice.InputSource? { get set }
```

```objc
@property (nonatomic, retain, nullable) AVCaptureDeviceInputSource * activeInputSource;
```

## Discussion

You must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) before attempting to set a format. Setting a format that isn’t present in the [`inputSources`](./inputsources.md) array results in an exception.

This property is key-value observable.

## See Also

### Configuring input sources
- [var inputSources: [AVCaptureDevice.InputSource]](./inputsources.md)
  An array of input sources that the device supports.
- [AVCaptureDevice.InputSource](./inputsource.md)
  A distinct input source on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeinputsource)*