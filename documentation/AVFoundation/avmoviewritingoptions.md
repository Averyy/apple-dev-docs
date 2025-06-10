# AVMovieWritingOptions

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines options to control the writing of a movie header to a destination URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct AVMovieWritingOptions
```

## Topics

### Writing Options
- [static var addMovieHeaderToDestination: AVMovieWritingOptions](avmoviewritingoptions/addmovieheadertodestination.md)
  The new movie header overwrites any existing movie header.
- [static var truncateDestinationToMovieHeaderOnly: AVMovieWritingOptions](avmoviewritingoptions/truncatedestinationtomovieheaderonly.md)
  The movie header overwrites all existing data and creates a pure reference movie file.
### Initializers
- [init(rawValue: UInt)](avmoviewritingoptions/init(rawvalue:).md)
  Creates a movie writing options structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func `is`(compatibleWithFileType: AVFileType) -> Bool](avmovie/is(compatiblewithfiletype:).md)
  Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [func makeMovieHeader(fileType: AVFileType) throws -> Data](avmovie/makemovieheader(filetype:).md)
  Creates a header for a movie for the specified file type.
- [func writeHeader(to: URL, fileType: AVFileType, options: AVMovieWritingOptions) throws](avmovie/writeheader(to:filetype:options:).md)
  Writes the movie header to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions)*