# setOutputSettings(_:for:)

**Framework**: AVFoundation  
**Kind**: method

Sets the options the output uses to encode media from the given connection while recording.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func setOutputSettings(_ outputSettings: [String : Any]?, for connection: AVCaptureConnection)
```

#### Discussion

For details on output settings, see [`Video settings`](video-settings.md) for video connections and [`Audio settings`](audio-settings.md) for audio connections.

On iOS, your output settings dictionary may only contain keys listed returned from the [`supportedOutputSettingsKeys(for:)`](avcapturemoviefileoutput/supportedoutputsettingskeys(for:).md) method. If you specify any other key, the system throws an invalid argument exception. Additionally, the value you specify for [`AVVideoCodecKey`](avvideocodeckey.md) should be present in the [`availableVideoCodecTypes`](avcapturemoviefileoutput/availablevideocodectypes.md) array. If you specify [`AVVideoCompressionPropertiesKey`](avvideocompressionpropertieskey.md), you must also specify a valid value for [`AVVideoCodecKey`](avvideocodeckey.md).

On iOS, the [`outputSettings(for:)`](avcapturemoviefileoutput/outputsettings(for:).md) method always provides a fully populated dictionary. If you call [`outputSettings(for:)`](avcapturemoviefileoutput/outputsettings(for:).md) with the intent of overriding a few of the values, you must exclude keys that aren’t supported before calling [`setOutputSettings(_:for:)`](avcapturemoviefileoutput/setoutputsettings(_:for:).md). When providing an [`AVVideoCompressionPropertiesKey`](avvideocompressionpropertieskey.md) sub dictionary, you may specify a sparse dictionary. A movie file output object always fills in missing keys with default values for the current capture session configuration.

## Parameters

- `outputSettings`: A dictionary of output settings. Pass an empty dictionary to specify that the format of the media from the connection shouldn’t change before writing to the file. Pass   to specify that the session preset determines output format.
- `connection`: The connection delivering the media to encode.

## See Also

- [func supportedOutputSettingsKeys(for: AVCaptureConnection) -> [String]](avcapturemoviefileoutput/supportedoutputsettingskeys(for:).md)
  Returns a list of supported keys to use in the output settings dictionary.
- [func outputSettings(for: AVCaptureConnection) -> [String : Any]](avcapturemoviefileoutput/outputsettings(for:).md)
  Returns the settings the output uses to encode media from the specified connection.
- [var availableVideoCodecTypes: [AVVideoCodecType]](avcapturemoviefileoutput/availablevideocodectypes.md)
  The video codecs types the output supports for recording movie files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/setoutputsettings(_:for:))*