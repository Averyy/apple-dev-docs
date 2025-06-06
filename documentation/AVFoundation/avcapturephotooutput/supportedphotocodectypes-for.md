# supportedPhotoCodecTypes(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns the list of photo codecs (such as JPEG or HEVC) supported for photo data in the specified file type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func supportedPhotoCodecTypes(for fileType: AVFileType) -> [AVVideoCodecType]
```

#### Return Value

An array of video codec types supported for encoding in the specified file type.

#### Discussion

When you issue a photo capture request, you can separately specify the format for capturing or encoding image data and the container format for producing output files containing that data. However, each file type supports only a specific set of image data types.

After choosing a file type from the [`availablePhotoFileTypes`](avcapturephotooutput/availablephotofiletypes.md) array, use this method to find a compatible image data codec before creating a photo settings object.

## Parameters

- `fileType`: The file type (such as JFIF or HEIF) for which to obtain codec information.

## See Also

- [var availablePhotoCodecTypes: [AVVideoCodecType]](avcapturephotooutput/availablephotocodectypes.md)
  The compression codecs this capture output currently supports for photo capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/supportedphotocodectypes(for:))*