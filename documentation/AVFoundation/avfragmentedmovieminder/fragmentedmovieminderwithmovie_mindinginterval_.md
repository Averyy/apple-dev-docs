# fragmentedMovieMinderWithMovie:mindingInterval:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a movie minder and adds a movie with a minding interval.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (instancetype) fragmentedMovieMinderWithMovie:(AVFragmentedMovie *) movie mindingInterval:(NSTimeInterval) mindingInterval;
```

## Return Value

A new `AVFragmentedMovieMinder` instance.

## Parameters

- `movie`: The fragmented movie object added to the movie minder.
- `mindingInterval`: The initial minding interval for the movie minder.

## See Also

### Creating a movie minder
- [init(movie: AVFragmentedMovie, mindingInterval: TimeInterval)](./init%28movie,mindinginterval%29.md)
  Creates a movie minder and adds a movie with a minding interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/fragmentedmovieminderwithmovie:mindinginterval:)*