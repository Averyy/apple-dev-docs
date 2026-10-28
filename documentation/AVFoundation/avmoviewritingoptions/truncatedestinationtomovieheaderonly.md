# truncateDestinationToMovieHeaderOnly

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The movie header overwrites all existing data and creates a pure reference movie file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var truncateDestinationToMovieHeaderOnly: AVMovieWritingOptions { get }
```

```c
AVMovieWritingTruncateDestinationToMovieHeaderOnly
```

## Discussion

Creates a file type box at the beginning of the destination file.

## See Also

### Writing options
- [static var addMovieHeaderToDestination: AVMovieWritingOptions](./addmovieheadertodestination.md)
  The new movie header overwrites any existing movie header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions/truncatedestinationtomovieheaderonly)*