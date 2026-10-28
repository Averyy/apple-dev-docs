# MPPlayableContentDataSource

**Framework**: Media Player  
**Kind**: protocol  
**Role**: Protocol

The data source providing media metadata to external media players so they can build user interfaces displaying your app’s content.

**Availability**:
- iOS 7.1+ - Deprecated in 14.0
- iPadOS 7.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
protocol MPPlayableContentDataSource : NSObjectProtocol
```

```objc
@protocol MPPlayableContentDataSource <NSObject>
```

## Overview

To support external media players, create a class that conforms to the `MPPlayableContentDataSource` protocol. When your app launches, create an instance of this class and assign it to the shared [`dataSource`](./mpplayablecontentmanager/datasource.md) property. This data source provides media metadata to external media players so that they can build user interfaces displaying your app’s content. It’s best to set this data source as early as possible in your app’s lifecycle, as iOS may start asking for content right away.

> ❗ **Important**:  This class is only used for CarPlay. Using it requires a special entitlement issued by Apple. Apps without the correct entitlement won’t appear on the CarPlay home screen. See [http://www.apple.com/ios/carplay/](http://www.apple.com/ios/carplay/) for more information.

## Topics

### Retrieving a media item
- [func contentItem(at: IndexPath) -> MPContentItem?](./mpplayablecontentdatasource/contentitem%28at%29.md)
  Retrieves the media item at the specified index.
- [func contentItem(forIdentifier: String, completionHandler: (MPContentItem?, (any Error)?) -> Void)](./mpplayablecontentdatasource/contentitem%28foridentifier,completionhandler%29.md)
  Retrieves the content item associated with the provided identifier.
### Working with child nodes
- [func beginLoadingChildItems(at: IndexPath, completionHandler: ((any Error)?) -> Void)](./mpplayablecontentdatasource/beginloadingchilditems%28at,completionhandler%29.md)
  Starts to load the children of the indicated index.
- [func childItemsDisplayPlaybackProgress(at: IndexPath) -> Bool](./mpplayablecontentdatasource/childitemsdisplayplaybackprogress%28at%29.md)
  Returns a Boolean value indicating whether the provided content supports playback progress.
- [func numberOfChildItems(at: IndexPath) -> Int](./mpplayablecontentdatasource/numberofchilditems%28at%29.md)
  Provides the number of child nodes for the indicated node.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Providing playable content
- [var dataSource: (any MPPlayableContentDataSource)?](./mpplayablecontentmanager/datasource.md)
  The data source provided by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource)*