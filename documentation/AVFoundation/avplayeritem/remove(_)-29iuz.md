# remove(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes the specified media data collector from the player item’s collection of media collectors.

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
func remove(_ collector: AVPlayerItemMediaDataCollector)
```

```objc
- (void) removeMediaDataCollector:(AVPlayerItemMediaDataCollector *) collector;
```

## Parameters

- `collector`: The instance of [`AVPlayerItemMediaDataCollector`](../avplayeritemmediadatacollector.md) to remove.

## See Also

### Managing player item data collectors
- [var mediaDataCollectors: [AVPlayerItemMediaDataCollector]](./mediadatacollectors.md)
  The collection of associated media data collectors.
- [func add(AVPlayerItemMediaDataCollector)](./add%28_%29-9l3to.md)
  Adds the specified media data collector to the player item’s collection of media collectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/remove(_:)-29iuz)*