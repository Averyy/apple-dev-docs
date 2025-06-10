# AVFragmentedMovieMinder

**Framework**: AVFoundation  
**Kind**: class

An object that checks whether a fragmented movie appends additional movie fragments.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class AVFragmentedMovieMinder
```

#### Overview

This class is identical to [`AVFragmentedAssetMinder`](avfragmentedassetminder.md) except that it’s capable of minding only assets of type [`AVFragmentedMovie`](avfragmentedmovie.md).

## Topics

### Creating a Movie Minder
- [init(movie: AVFragmentedMovie, mindingInterval: TimeInterval)](avfragmentedmovieminder/init(movie:mindinginterval:).md)
  Creates a movie minder and adds a movie with a minding interval.
### Adding and Removing Movies
- [var movies: [AVFragmentedMovie]](avfragmentedmovieminder/movies.md)
  An array containing the fragmented movie objects being minded.
- [func add(AVFragmentedMovie)](avfragmentedmovieminder/add(_:).md)
  Adds a fragmented movie to the array of movies being minded.
- [func remove(AVFragmentedMovie)](avfragmentedmovieminder/remove(_:).md)
  Removes a fragmented movie from the array of movies being minded.
### Accessing Minder Information
- [var mindingInterval: TimeInterval](avfragmentedmovieminder/mindinginterval.md)
  The amount of time between checks for additional movie fragments.

## Relationships

### Inherits From
- [AVFragmentedAssetMinder](avfragmentedassetminder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVFragmentedMovie](avfragmentedmovie.md)
  An object that represents a fragmented movie file.
- [class AVFragmentedMovieTrack](avfragmentedmovietrack.md)
  An object that represents a track in a fragmented movie.
- [protocol AVFragmentMinding](avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder)*