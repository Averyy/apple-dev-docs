# availableVideoCodecTypes

**Framework**: AVFoundation  
**Kind**: property

The video codecs types the output supports for recording movie files.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var availableVideoCodecTypes: [AVVideoCodecType] { get }
```

#### Discussion

The first codec in this list is the default for recording movie files. To record using a different codec, call the [`setOutputSettings(_:for:)`](avcapturemoviefileoutput/setoutputsettings(_:for:).md) method, passing a video settings dictionary with a value for [`AVVideoCodecKey`](avvideocodeckey.md) that matches one of the other values in this list.

## See Also

- [func supportedOutputSettingsKeys(for: AVCaptureConnection) -> [String]](avcapturemoviefileoutput/supportedoutputsettingskeys(for:).md)
  Returns a list of supported keys to use in the output settings dictionary.
- [func outputSettings(for: AVCaptureConnection) -> [String : Any]](avcapturemoviefileoutput/outputsettings(for:).md)
  Returns the settings the output uses to encode media from the specified connection.
- [func setOutputSettings([String : Any]?, for: AVCaptureConnection)](avcapturemoviefileoutput/setoutputsettings(_:for:).md)
  Sets the options the output uses to encode media from the given connection while recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/availablevideocodectypes)*