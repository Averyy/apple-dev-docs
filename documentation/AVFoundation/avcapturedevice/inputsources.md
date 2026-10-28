# inputSources

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of input sources that the device supports.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var inputSources: [AVCaptureDevice.InputSource] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVCaptureDeviceInputSource *> * inputSources;
```

## Discussion

Some devices can capture data from one of multiple data sources (different input jacks on the same audio device, for example). For devices with multiple possible data sources, you can use this property to enumerate the possible choices.

This value is key-value observable.

## See Also

### Configuring input sources
- [var activeInputSource: AVCaptureDevice.InputSource?](./activeinputsource.md)
  The currently active input source of the device.
- [AVCaptureDevice.InputSource](./inputsource.md)
  A distinct input source on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/inputsources)*