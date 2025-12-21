# producesCombinableFragments

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var producesCombinableFragments: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). Set the value to [`true`](https://developer.apple.com/documentation/Swift/true) when you use multiple asset writers to produce distinct streams that complement each other, such as HLS encodings or bit rate variants.

You can’t set this property after writing starts.

## See Also

- [var movieFragmentInterval: CMTime](avassetwriter/moviefragmentinterval.md)
  The interval at which to write movie fragments.
- [var initialMovieFragmentInterval: CMTime](avassetwriter/initialmoviefragmentinterval.md)
  The interval at which to write the initial movie fragment.
- [var initialMovieFragmentSequenceNumber: Int](avassetwriter/initialmoviefragmentsequencenumber.md)
  The sequence number of the initial movie fragment.
- [var overallDurationHint: CMTime](avassetwriter/overalldurationhint.md)
  A hint of the final duration of the output file.
- [var movieTimeScale: CMTimeScale](avassetwriter/movietimescale.md)
  The time scale of the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/producescombinablefragments)*