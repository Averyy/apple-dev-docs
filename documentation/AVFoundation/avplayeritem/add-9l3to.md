# add(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds the specified media data collector to the player item’s collection of media collectors.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.3+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.3+

## Declaration

```swift
nonisolated
func add(_ collector: AVPlayerItemMediaDataCollector)
```

#### Discussion

This method may incur additional I/O to collect the requested media data asynchronously.

## Parameters

- `collector`: An instance of  .

## See Also

- [var mediaDataCollectors: [AVPlayerItemMediaDataCollector]](avplayeritem/mediadatacollectors.md)
  The collection of associated media data collectors.
- [func remove(AVPlayerItemMediaDataCollector)](avplayeritem/remove(_:)-29iuz.md)
  Removes the specified media data collector from the player item’s collection of media collectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/add(_:)-9l3to)*