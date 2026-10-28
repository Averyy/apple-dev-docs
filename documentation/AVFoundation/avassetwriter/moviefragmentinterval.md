# movieFragmentInterval

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The interval at which to write movie fragments.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var movieFragmentInterval: CMTime { get set }
```

```objc
@property (nonatomic) CMTime movieFragmentInterval;
```

## Discussion

Some container formats, such as QuickTime movies, support writing movies in fragments. Using this feature enables you to open and play a partially written movie in the event that an unexpected error or interruption occurs.

An asset writer disables this feature by default and sets this value to [`invalid`](../../CoreMedia/cmtime/invalid.md). To enable fragment writing, set a valid [`CMTime`](../../CoreMedia/cmtime.md) value. For best performance when writing to external storage devices, set the movie fragment interval to 10 seconds or greater.

You can’t set this value after writing starts.

## See Also

### Configuring fragment output
- [var initialMovieFragmentInterval: CMTime](./initialmoviefragmentinterval.md)
  The interval at which to write the initial movie fragment.
- [var initialMovieFragmentSequenceNumber: Int](./initialmoviefragmentsequencenumber.md)
  The sequence number of the initial movie fragment.
- [var producesCombinableFragments: Bool](./producescombinablefragments.md)
  A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [var overallDurationHint: CMTime](./overalldurationhint.md)
  A hint of the final duration of the output file.
- [var movieTimeScale: CMTimeScale](./movietimescale.md)
  The time scale of the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/moviefragmentinterval)*