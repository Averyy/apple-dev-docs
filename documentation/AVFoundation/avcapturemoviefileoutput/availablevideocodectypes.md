# availableVideoCodecTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availableVideoCodecTypes;
```

#### Discussion

The first codec in this list is the default for recording movie files. To record using a different codec, call the [`setOutputSettings(_:for:)`](./setoutputsettings%28_,for%29.md) method, passing a video settings dictionary with a value for [`AVVideoCodecKey`](../avvideocodeckey.md) that matches one of the other values in this list.

## See Also

### Managing output settings
- [func supportedOutputSettingsKeys(for: AVCaptureConnection) -> [String]](./supportedoutputsettingskeys%28for%29.md)
  Returns a list of supported keys to use in the output settings dictionary.
- [func outputSettings(for: AVCaptureConnection) -> [String : Any]](./outputsettings%28for%29.md)
  Returns the settings the output uses to encode media from the specified connection.
- [func setOutputSettings([String : Any]?, for: AVCaptureConnection)](./setoutputsettings%28_,for%29.md)
  Sets the options the output uses to encode media from the given connection while recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/availablevideocodectypes)*