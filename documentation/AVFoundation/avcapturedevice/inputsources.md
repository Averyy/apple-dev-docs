# inputSources

**Framework**: AVFoundation  
**Kind**: property

An array of input sources that the device supports.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var inputSources: [AVCaptureDevice.InputSource] { get }
```

#### Discussion

Some devices can capture data from one of multiple data sources (different input jacks on the same audio device, for example). For devices with multiple possible data sources, you can use this property to enumerate the possible choices.

This value is key-value observable.

## See Also

- [var activeInputSource: AVCaptureDevice.InputSource?](avcapturedevice/activeinputsource.md)
  The currently active input source of the device.
- [AVCaptureDevice.InputSource](avcapturedevice/inputsource.md)
  A distinct input source on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/inputsources)*