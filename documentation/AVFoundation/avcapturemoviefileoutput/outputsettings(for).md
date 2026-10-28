# outputSettings(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the settings the output uses to encode media from the specified connection.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func outputSettings(for connection: AVCaptureConnection) -> [String : Any]
```

```objc
- (NSDictionary<NSString *,id> *) outputSettingsForConnection:(AVCaptureConnection *) connection;
```

## Return Value

A dictionary of output settings.

## Discussion

If the returned value is an empty dictionary, the format of the media from the connection isn’t changed before writing to the file.

If you call [`setOutputSettings(_:for:)`](./setoutputsettings%28_,for%29.md) with a `nil` dictionary, this method returns a non-`nil` dictionary that reflects the settings used by the capture session’s [`sessionPreset`](../avcapturesession/sessionpreset.md) value.

## Parameters

- `connection`: The connection delivering the media to encode.

## See Also

### Managing output settings
- [func supportedOutputSettingsKeys(for: AVCaptureConnection) -> [String]](./supportedoutputsettingskeys%28for%29.md)
  Returns a list of supported keys to use in the output settings dictionary.
- [func setOutputSettings([String : Any]?, for: AVCaptureConnection)](./setoutputsettings%28_,for%29.md)
  Sets the options the output uses to encode media from the given connection while recording.
- [var availableVideoCodecTypes: [AVVideoCodecType]](./availablevideocodectypes.md)
  The video codecs types the output supports for recording movie files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/outputsettings(for:))*