# makeMovieHeader(fileType:)

**Framework**: AVFoundation  
**Kind**: method

Creates a header for a movie for the specified file type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func makeMovieHeader(fileType: AVFileType) throws -> Data
```

#### Return Value

An [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing the movie header.

#### Discussion

The created movie header is a pure reference movie, with no base URL, suitable for use on the pasteboard.

## Parameters

- `fileType`: A UTI that indicates the specific file format for the movie header.

## See Also

- [func `is`(compatibleWithFileType: AVFileType) -> Bool](avmovie/is(compatiblewithfiletype:).md)
  Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [func writeHeader(to: URL, fileType: AVFileType, options: AVMovieWritingOptions) throws](avmovie/writeheader(to:filetype:options:).md)
  Writes the movie header to the specified URL.
- [struct AVMovieWritingOptions](avmoviewritingoptions.md)
  A structure that defines options to control the writing of a movie header to a destination URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/makemovieheader(filetype:))*