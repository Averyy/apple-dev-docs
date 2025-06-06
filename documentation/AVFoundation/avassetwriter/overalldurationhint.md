# overallDurationHint

**Framework**: AVFoundation  
**Kind**: property

A hint of the final duration of the output file.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var overallDurationHint: CMTime { get set }
```

#### Discussion

The default value of [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid) indicates that the asset writer doesn’t write an overall duration hint to the file. The asset writer ignores this value if it doesn’t write movie fragments.

You can’t set this property after writing starts.

## See Also

- [var movieFragmentInterval: CMTime](avassetwriter/moviefragmentinterval.md)
  The interval at which to write movie fragments.
- [var initialMovieFragmentInterval: CMTime](avassetwriter/initialmoviefragmentinterval.md)
  The interval at which to write the initial movie fragment.
- [var initialMovieFragmentSequenceNumber: Int](avassetwriter/initialmoviefragmentsequencenumber.md)
  The sequence number of the initial movie fragment.
- [var producesCombinableFragments: Bool](avassetwriter/producescombinablefragments.md)
  A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [var movieTimeScale: CMTimeScale](avassetwriter/movietimescale.md)
  The time scale of the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/overalldurationhint)*