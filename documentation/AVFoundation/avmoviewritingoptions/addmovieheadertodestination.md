# addMovieHeaderToDestination

**Framework**: AVFoundation  
**Kind**: property

The new movie header overwrites any existing movie header.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var addMovieHeaderToDestination: AVMovieWritingOptions { get }
```

#### Discussion

Only an existing movie header is overwritten, all other data is preserved. If the destination file is empty, a file type box is created at the beginning of the file.

## See Also

- [static var truncateDestinationToMovieHeaderOnly: AVMovieWritingOptions](avmoviewritingoptions/truncatedestinationtomovieheaderonly.md)
  The movie header overwrites all existing data and creates a pure reference movie file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions/addmovieheadertodestination)*