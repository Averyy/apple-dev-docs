# AVMovieWritingOptions

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum AVMovieWritingOptions : NSUInteger;
```

## Topics

### Writing options
- [static var addMovieHeaderToDestination: AVMovieWritingOptions](./avmoviewritingoptions/addmovieheadertodestination.md)
  The new movie header overwrites any existing movie header.
- [static var truncateDestinationToMovieHeaderOnly: AVMovieWritingOptions](./avmoviewritingoptions/truncatedestinationtomovieheaderonly.md)
  The movie header overwrites all existing data and creates a pure reference movie file.
### Initializers
- [init(rawValue: UInt)](./avmoviewritingoptions/init%28rawvalue%29.md)
  Creates a movie writing options structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Creating and writing headers
- [func `is`(compatibleWithFileType: AVFileType) -> Bool](./avmovie/is%28compatiblewithfiletype%29.md)
  Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [func makeMovieHeader(fileType: AVFileType) throws -> Data](./avmovie/makemovieheader%28filetype%29.md)
  Creates a header for a movie for the specified file type.
- [func writeHeader(to: URL, fileType: AVFileType, options: AVMovieWritingOptions) throws](./avmovie/writeheader%28to,filetype,options%29.md)
  Writes the movie header to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions)*