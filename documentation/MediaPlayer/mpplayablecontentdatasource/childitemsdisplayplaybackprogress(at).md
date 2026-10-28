# childItemsDisplayPlaybackProgress(at:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the provided content supports playback progress.

**Availability**:
- iOS 7.1+ - Deprecated in 14.0
- iPadOS 7.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
optional func childItemsDisplayPlaybackProgress(at indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) childItemsDisplayPlaybackProgressAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the indicated media item supports displaying playback progress.

## Discussion

If this method isn’t implemented, playback progress is not supported for any media item. If any media item does support displaying the playback progress, you must implement this method.

## Parameters

- `indexPath`: The index of the media item being queried.

## See Also

### Working with child nodes
- [func beginLoadingChildItems(at: IndexPath, completionHandler: ((any Error)?) -> Void)](./beginloadingchilditems%28at,completionhandler%29.md)
  Starts to load the children of the indicated index.
- [func numberOfChildItems(at: IndexPath) -> Int](./numberofchilditems%28at%29.md)
  Provides the number of child nodes for the indicated node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/childitemsdisplayplaybackprogress(at:))*