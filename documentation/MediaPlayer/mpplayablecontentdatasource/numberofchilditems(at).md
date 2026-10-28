# numberOfChildItems(at:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the number of child nodes for the indicated node.

**Availability**:
- iOS 7.1+ - Deprecated in 14.0
- iPadOS 7.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
func numberOfChildItems(at indexPath: IndexPath) -> Int
```

```objc
- (NSInteger) numberOfChildItemsAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

An [`NSInteger`](../../ObjectiveC/nsinteger.md) value representing the number of child nodes associated with the indicated node.

## Parameters

- `indexPath`: The index for the node to be queried.

## See Also

### Working with child nodes
- [func beginLoadingChildItems(at: IndexPath, completionHandler: ((any Error)?) -> Void)](./beginloadingchilditems%28at,completionhandler%29.md)
  Starts to load the children of the indicated index.
- [func childItemsDisplayPlaybackProgress(at: IndexPath) -> Bool](./childitemsdisplayplaybackprogress%28at%29.md)
  Returns a Boolean value indicating whether the provided content supports playback progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/numberofchilditems(at:))*