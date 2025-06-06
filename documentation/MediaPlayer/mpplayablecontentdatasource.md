# MPPlayableContentDataSource

**Framework**: Media Player  
**Kind**: protocol

The data source providing media metadata to external media players so they can build user interfaces displaying your app’s content.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol MPPlayableContentDataSource : NSObjectProtocol
```

#### Overview

To support external media players, create a class that conforms to the `MPPlayableContentDataSource` protocol. When your app launches, create an instance of this class and assign it to the shared [`dataSource`](mpplayablecontentmanager/datasource.md) property. This data source provides media metadata to external media players so that they can build user interfaces displaying your app’s content. It’s best to set this data source as early as possible in your app’s lifecycle, as iOS may start asking for content right away.

> ❗ **Important**:  This class is only used for CarPlay. Using it requires a special entitlement issued by Apple. Apps without the correct entitlement won’t appear on the CarPlay home screen. See [`http://www.apple.com/ios/carplay/`](https://developer.apple.comhttp://www.apple.com/ios/carplay/) for more information.

 This class is only used for CarPlay. Using it requires a special entitlement issued by Apple. Apps without the correct entitlement won’t appear on the CarPlay home screen. See [`http://www.apple.com/ios/carplay/`](https://developer.apple.comhttp://www.apple.com/ios/carplay/) for more information.

## Topics

### Retrieving a media item
- [func contentItem(at: IndexPath) -> MPContentItem?](mpplayablecontentdatasource/contentitem(at:).md)
  Retrieves the media item at the specified index.
- [func contentItem(forIdentifier: String, completionHandler: (MPContentItem?, (any Error)?) -> Void)](mpplayablecontentdatasource/contentitem(foridentifier:completionhandler:).md)
  Retrieves the content item associated with the provided identifier.
### Working with child nodes
- [func beginLoadingChildItems(at: IndexPath, completionHandler: ((any Error)?) -> Void)](mpplayablecontentdatasource/beginloadingchilditems(at:completionhandler:).md)
  Starts to load the children of the indicated index.
- [func childItemsDisplayPlaybackProgress(at: IndexPath) -> Bool](mpplayablecontentdatasource/childitemsdisplayplaybackprogress(at:).md)
  Returns a Boolean value indicating whether the provided content supports playback progress.
- [func numberOfChildItems(at: IndexPath) -> Int](mpplayablecontentdatasource/numberofchilditems(at:).md)
  Provides the number of child nodes for the indicated node.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var dataSource: (any MPPlayableContentDataSource)?](mpplayablecontentmanager/datasource.md)
  The data source provided by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource)*