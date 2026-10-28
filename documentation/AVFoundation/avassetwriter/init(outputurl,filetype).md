# init(outputURL:fileType:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an object that writes media data to a container file at the output URL.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(outputURL: URL, fileType outputFileType: AVFileType) throws
```

```objc
- (instancetype) initWithURL:(NSURL *) outputURL fileType:(AVFileType) outputFileType error:(NSError **) outError;
```

## Discussion

Writing fails if a file already exists at the output URL.

## Parameters

- `outputURL`: The location of the file to write.
- `outputFileType`: The type of container file to write.

## See Also

### Creating an asset writer
- [convenience init(url: URL, fileType: AVFileType) throws](./init%28url,filetype%29-xt34.md)
  Returns a new object that writes media data to a container file at the output URL.
- [init(contentType: UTType)](./init%28contenttype%29.md)
  Creates an object that outputs segment data in a specified container format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/init(outputurl:filetype:))*