# beginLoadingChildItems(at:completionHandler:)

**Framework**: Media Player  
**Kind**: method

Starts to load the children of the indicated index.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func beginLoadingChildItems(at indexPath: IndexPath) async throws
```

#### Discussion

Call this method to start asynchronous batch loading of media items. The app can load content before the media player needs to display the next media items. When you use this method, the client app must call the completion handler after loading has finished.

## Parameters

- `indexPath`: The index of the current item.
- `completionHandler`: A block to be called after all loading is completed. The block receives the following parameter: - ***error***: Contains an error message if there was an error trying to load the children of the indicated item; otherwise, contains `nil`.

## See Also

- [func childItemsDisplayPlaybackProgress(at: IndexPath) -> Bool](mpplayablecontentdatasource/childitemsdisplayplaybackprogress(at:).md)
  Returns a Boolean value indicating whether the provided content supports playback progress.
- [func numberOfChildItems(at: IndexPath) -> Int](mpplayablecontentdatasource/numberofchilditems(at:).md)
  Provides the number of child nodes for the indicated node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/beginloadingchilditems(at:completionhandler:))*