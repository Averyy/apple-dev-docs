# movieTimeScale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time scale of the movie.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var movieTimeScale: CMTimeScale { get set }
```

```objc
@property (nonatomic) CMTimeScale movieTimeScale;
```

#### Discussion

The default value is `0`, which indicates that the asset writer chooses an appropriate value, if applicable.

You can’t set this property value after writing starts.

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
- [var overallDurationHint: CMTime](./overalldurationhint.md)
  A hint of the final duration of the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/movietimescale)*