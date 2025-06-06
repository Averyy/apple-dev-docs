# numberOfChildItems(at:)

**Framework**: Media Player  
**Kind**: method  
**Required**: Yes

Provides the number of child nodes for the indicated node.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func numberOfChildItems(at indexPath: IndexPath) -> Int
```

#### Return Value

An [`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger) value representing the number of child nodes associated with the indicated node.

## Parameters

- `indexPath`: The index for the node to be queried.

## See Also

- [func beginLoadingChildItems(at: IndexPath, completionHandler: ((any Error)?) -> Void)](mpplayablecontentdatasource/beginloadingchilditems(at:completionhandler:).md)
  Starts to load the children of the indicated index.
- [func childItemsDisplayPlaybackProgress(at: IndexPath) -> Bool](mpplayablecontentdatasource/childitemsdisplayplaybackprogress(at:).md)
  Returns a Boolean value indicating whether the provided content supports playback progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/numberofchilditems(at:))*