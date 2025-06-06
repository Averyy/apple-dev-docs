# supportedOutputSettingsKeys(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns a list of supported keys to use in the output settings dictionary.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func supportedOutputSettingsKeys(for connection: AVCaptureConnection) -> [String]
```

#### Return Value

An array of keys that can be set in the [`setOutputSettings(_:for:)`](avcapturemoviefileoutput/setoutputsettings(_:for:).md)method.

## Parameters

- `connection`: The connection that delivers the media to encode.

## See Also

- [func outputSettings(for: AVCaptureConnection) -> [String : Any]](avcapturemoviefileoutput/outputsettings(for:).md)
  Returns the settings the output uses to encode media from the specified connection.
- [func setOutputSettings([String : Any]?, for: AVCaptureConnection)](avcapturemoviefileoutput/setoutputsettings(_:for:).md)
  Sets the options the output uses to encode media from the given connection while recording.
- [var availableVideoCodecTypes: [AVVideoCodecType]](avcapturemoviefileoutput/availablevideocodectypes.md)
  The video codecs types the output supports for recording movie files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/supportedoutputsettingskeys(for:))*