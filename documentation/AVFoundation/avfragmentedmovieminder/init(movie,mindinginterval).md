# init(movie:mindingInterval:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a movie minder and adds a movie with a minding interval.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(movie: AVFragmentedMovie, mindingInterval: TimeInterval)
```

```objc
- (instancetype) initWithMovie:(AVFragmentedMovie *) movie mindingInterval:(NSTimeInterval) mindingInterval;
```

#### Return Value

A new `AVFragmentedMovieMinder` instance.

## Parameters

- `movie`: The fragmented movie object added to the movie minder.
- `mindingInterval`: The initial minding interval for the movie minder.

## See Also

### Creating a movie minder
- [+ fragmentedMovieMinderWithMovie:mindingInterval:](./fragmentedmovieminderwithmovie_mindinginterval_.md)
  Creates a movie minder and adds a movie with a minding interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/init(movie:mindinginterval:))*