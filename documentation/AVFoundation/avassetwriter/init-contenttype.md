# init(contentType:)

**Framework**: AVFoundation  
**Kind**: init

Creates an object that outputs segment data in a specified container format.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(contentType outputContentType: UTType)
```

#### Discussion

Use this initializer to create an asset writer that outputs segment data to an adopter of the [`AVAssetWriterDelegate`](avassetwriterdelegate.md) protocol. For example, you can create an asset writer object to write an MPEG-4 file as shown below:

```swift
// Create a UTType for the MP4 file type.
guard let contentType = UTType(AVFileType.mp4.rawValue) else { return }
let assetWriter = AVAssetWriter(contentType: contentType)
```

## Parameters

- `outputContentType`: A type that indicates the format of the segment data to output.

## See Also

- [convenience init(url: URL, fileType: AVFileType) throws](avassetwriter/init(url:filetype:).md)
  Returns a new object that writes media data to a container file at the output URL.
- [init(outputURL: URL, fileType: AVFileType) throws](avassetwriter/init(outputurl:filetype:).md)
  Creates an object that writes media data to a container file at the output URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/init(contenttype:))*