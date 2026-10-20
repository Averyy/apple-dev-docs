# canContainMovieFragments

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether fragments can extend the movie file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var canContainMovieFragments: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canContainMovieFragments;
```

#### Discussion

The value of this property is `YES` if an `mvex` box is present in the `moov` box. The `mvex` box is necessary to signal the possible presence of later `moof` boxes.

## See Also

### Determining fragment support
- [var containsMovieFragments: Bool](./containsmoviefragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the movie file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/cancontainmoviefragments)*