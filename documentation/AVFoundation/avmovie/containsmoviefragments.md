# containsMovieFragments

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether at least one movie fragment extends the movie file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var containsMovieFragments: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL containsMovieFragments;
```

## Discussion

This property is `YES` if [`canContainMovieFragments`](./cancontainmoviefragments.md) is `YES` and at least one `moof` box is present after the `moov` box.

## See Also

### Determining fragment support
- [var canContainMovieFragments: Bool](./cancontainmoviefragments.md)
  A Boolean value that indicates whether fragments can extend the movie file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/containsmoviefragments)*