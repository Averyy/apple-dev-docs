# availablePhotoCodecTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The compression codecs this capture output currently supports for photo capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var availablePhotoCodecTypes: [AVVideoCodecType] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availablePhotoCodecTypes;
```

#### Discussion

To capture a photo in a compressed format, such as JPEG, use the [`init(format:)`](../avcapturephotosettings/init%28format%29.md) initializer to create your photo settings object. In that initializer’s `format` dictionary, pass the key [`AVVideoCodecKey`](../avvideocodeckey.md), whose value must be one of the codec identifiers listed in this array.

> **Note**:  Read this property only after adding the photo capture output to an [`AVCaptureSession`](../avcapturesession.md) object containing a video source. If the photo capture output isn’t connected to a session with a video source, this array is empty.

This property supports key-value observing.

## See Also

### Determining supported codec types
- [func supportedPhotoCodecTypes(for: AVFileType) -> [AVVideoCodecType]](./supportedphotocodectypes%28for%29.md)
  Returns the list of photo codecs (such as JPEG or HEVC) supported for photo data in the specified file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablephotocodectypes)*