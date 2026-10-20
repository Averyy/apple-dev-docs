# is(compatibleWithFileType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the system can create a movie header of the specified type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func `is`(compatibleWithFileType fileType: AVFileType) -> Bool
```

```objc
- (BOOL) isCompatibleWithFileType:(AVFileType) fileType;
```

#### Return Value

[`true`](../../Swift/true.md) if the movie only contains tracks whose media types are allowed by the specified file type; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `fileType`: A file type to test.

## See Also

### Creating and writing headers
- [func makeMovieHeader(fileType: AVFileType) throws -> Data](./makemovieheader%28filetype%29.md)
  Creates a header for a movie for the specified file type.
- [func writeHeader(to: URL, fileType: AVFileType, options: AVMovieWritingOptions) throws](./writeheader%28to,filetype,options%29.md)
  Writes the movie header to the specified URL.
- [struct AVMovieWritingOptions](../avmoviewritingoptions.md)
  A structure that defines options to control the writing of a movie header to a destination URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/is(compatiblewithfiletype:))*