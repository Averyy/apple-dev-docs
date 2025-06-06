# writeHeader(to:fileType:options:)

**Framework**: AVFoundation  
**Kind**: method

Writes the movie header to the specified URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func writeHeader(to URL: URL, fileType: AVFileType, options: AVMovieWritingOptions = []) throws
```

## Parameters

- `URL`: The URL indicating where to write the movie header.
- `fileType`: A UTI that indicates the specific file format for the movie header.
- `options`: The   constants whose bits specify the options for writing the movie header.

## See Also

- [func `is`(compatibleWithFileType: AVFileType) -> Bool](avmovie/is(compatiblewithfiletype:).md)
  Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [func makeMovieHeader(fileType: AVFileType) throws -> Data](avmovie/makemovieheader(filetype:).md)
  Creates a header for a movie for the specified file type.
- [struct AVMovieWritingOptions](avmoviewritingoptions.md)
  A structure that defines options to control the writing of a movie header to a destination URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/writeheader(to:filetype:options:))*