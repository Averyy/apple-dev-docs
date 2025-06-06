# initialMovieFragmentSequenceNumber

**Framework**: AVFoundation  
**Kind**: property

The sequence number of the initial movie fragment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var initialMovieFragmentSequenceNumber: Int { get set }
```

#### Discussion

If you combine movie fragments that you create from multiple asset writers, movie fragment sequence numbers need to increase monotonically across the entire combined collection, in temporal order. The default value of this property is `1`.

You can’t set this property after writing starts.

## See Also

- [var movieFragmentInterval: CMTime](avassetwriter/moviefragmentinterval.md)
  The interval at which to write movie fragments.
- [var initialMovieFragmentInterval: CMTime](avassetwriter/initialmoviefragmentinterval.md)
  The interval at which to write the initial movie fragment.
- [var producesCombinableFragments: Bool](avassetwriter/producescombinablefragments.md)
  A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [var overallDurationHint: CMTime](avassetwriter/overalldurationhint.md)
  A hint of the final duration of the output file.
- [var movieTimeScale: CMTimeScale](avassetwriter/movietimescale.md)
  The time scale of the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/initialmoviefragmentsequencenumber)*