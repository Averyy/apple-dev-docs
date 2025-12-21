# childItemsDisplayPlaybackProgress(at:)

**Framework**: Media Player  
**Kind**: method

Returns a Boolean value indicating whether the provided content supports playback progress.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func childItemsDisplayPlaybackProgress(at indexPath: IndexPath) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the indicated media item supports displaying playback progress.

#### Discussion

If this method isn’t implemented, playback progress is not supported for any media item. If any media item does support displaying the playback progress, you must implement this method.

## Parameters

- `indexPath`: The index of the media item being queried.

## See Also

- [func beginLoadingChildItems(at: IndexPath, completionHandler: ((any Error)?) -> Void)](mpplayablecontentdatasource/beginloadingchilditems(at:completionhandler:).md)
  Starts to load the children of the indicated index.
- [func numberOfChildItems(at: IndexPath) -> Int](mpplayablecontentdatasource/numberofchilditems(at:).md)
  Provides the number of child nodes for the indicated node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/childitemsdisplayplaybackprogress(at:))*