# writeHeader(to:fileType:options:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) writeMovieHeaderToURL:(NSURL *) URL fileType:(AVFileType) fileType options:(AVMovieWritingOptions) options error:(NSError **) outError;
```

## Parameters

- `URL`: The URL indicating where to write the movie header.
- `fileType`: A UTI that indicates the specific file format for the movie header.
- `options`: The [`AVMovieWritingOptions`](../avmoviewritingoptions.md) constants whose bits specify the options for writing the movie header.

## See Also

### Creating and writing headers
- [func `is`(compatibleWithFileType: AVFileType) -> Bool](./is%28compatiblewithfiletype%29.md)
  Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [func makeMovieHeader(fileType: AVFileType) throws -> Data](./makemovieheader%28filetype%29.md)
  Creates a header for a movie for the specified file type.
- [struct AVMovieWritingOptions](../avmoviewritingoptions.md)
  A structure that defines options to control the writing of a movie header to a destination URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/writeheader(to:filetype:options:))*