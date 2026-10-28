# AVFragmentedMovieMinder

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVFragmentedMovieMinder : AVFragmentedAssetMinder
```

## Overview

This class is identical to [`AVFragmentedAssetMinder`](./avfragmentedassetminder.md) except that it’s capable of minding only assets of type [`AVFragmentedMovie`](./avfragmentedmovie.md).

## Topics

### Creating a movie minder
- [init(movie: AVFragmentedMovie, mindingInterval: TimeInterval)](./avfragmentedmovieminder/init%28movie,mindinginterval%29.md)
  Creates a movie minder and adds a movie with a minding interval.
- [+ fragmentedMovieMinderWithMovie:mindingInterval:](./avfragmentedmovieminder/fragmentedmovieminderwithmovie_mindinginterval_.md)
  Creates a movie minder and adds a movie with a minding interval.
### Adding and removing movies
- [var movies: [AVFragmentedMovie]](./avfragmentedmovieminder/movies.md)
  An array containing the fragmented movie objects being minded.
- [func add(AVFragmentedMovie)](./avfragmentedmovieminder/add%28_%29.md)
  Adds a fragmented movie to the array of movies being minded.
- [func remove(AVFragmentedMovie)](./avfragmentedmovieminder/remove%28_%29.md)
  Removes a fragmented movie from the array of movies being minded.
### Accessing minder information
- [var mindingInterval: TimeInterval](./avfragmentedmovieminder/mindinginterval.md)
  The amount of time between checks for additional movie fragments.

## Relationships

### Inherits From
- [AVFragmentedAssetMinder](./avfragmentedassetminder.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Fragmented movies
- [class AVFragmentedMovie](./avfragmentedmovie.md)
  An object that represents a fragmented movie file.
- [class AVFragmentedMovieTrack](./avfragmentedmovietrack.md)
  An object that represents a track in a fragmented movie.
- [protocol AVFragmentMinding](./avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder)*