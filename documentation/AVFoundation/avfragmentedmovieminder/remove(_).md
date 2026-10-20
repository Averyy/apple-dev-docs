# remove(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes a fragmented movie from the array of movies being minded.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func remove(_ movie: AVFragmentedMovie)
```

```objc
- (void) removeFragmentedMovie:(AVFragmentedMovie *) movie;
```

## Parameters

- `movie`: The fragmented movie removed from the minder.

## See Also

### Adding and removing movies
- [var movies: [AVFragmentedMovie]](./movies.md)
  An array containing the fragmented movie objects being minded.
- [func add(AVFragmentedMovie)](./add%28_%29.md)
  Adds a fragmented movie to the array of movies being minded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/remove(_:))*