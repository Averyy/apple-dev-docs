# is(compatibleWithFileType:)

**Framework**: AVFoundation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the movie only contains tracks whose media types are allowed by the specified file type; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `fileType`: A file type to test.

## See Also

- [func makeMovieHeader(fileType: AVFileType) throws -> Data](avmovie/makemovieheader(filetype:).md)
  Creates a header for a movie for the specified file type.
- [func writeHeader(to: URL, fileType: AVFileType, options: AVMovieWritingOptions) throws](avmovie/writeheader(to:filetype:options:).md)
  Writes the movie header to the specified URL.
- [struct AVMovieWritingOptions](avmoviewritingoptions.md)
  A structure that defines options to control the writing of a movie header to a destination URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/is(compatiblewithfiletype:))*