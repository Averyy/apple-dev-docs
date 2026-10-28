# overallDurationHint

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) CMTime overallDurationHint;
```

## Discussion

The default value of [`invalid`](../../CoreMedia/cmtime/invalid.md) indicates that the asset writer doesn’t write an overall duration hint to the file. The asset writer ignores this value if it doesn’t write movie fragments.

You can’t set this property after writing starts.

## See Also

### Configuring fragment output
- [var movieFragmentInterval: CMTime](./moviefragmentinterval.md)
  The interval at which to write movie fragments.
- [var initialMovieFragmentInterval: CMTime](./initialmoviefragmentinterval.md)
  The interval at which to write the initial movie fragment.
- [var initialMovieFragmentSequenceNumber: Int](./initialmoviefragmentsequencenumber.md)
  The sequence number of the initial movie fragment.
- [var producesCombinableFragments: Bool](./producescombinablefragments.md)
  A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [var movieTimeScale: CMTimeScale](./movietimescale.md)
  The time scale of the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/overalldurationhint)*