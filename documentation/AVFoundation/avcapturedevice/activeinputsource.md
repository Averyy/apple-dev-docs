# activeInputSource

**Framework**: AVFoundation  
**Kind**: property

The currently active input source of the device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var activeInputSource: AVCaptureDevice.InputSource? { get set }
```

#### Discussion

You must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) before attempting to set a format. Setting a format that isn’t present in the [`inputSources`](avcapturedevice/inputsources.md) array results in an exception.

This property is key-value observable.

## See Also

- [var inputSources: [AVCaptureDevice.InputSource]](avcapturedevice/inputsources.md)
  An array of input sources that the device supports.
- [AVCaptureDevice.InputSource](avcapturedevice/inputsource.md)
  A distinct input source on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeinputsource)*