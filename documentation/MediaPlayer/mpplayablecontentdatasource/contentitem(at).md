# contentItem(at:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Retrieves the media item at the specified index.

**Availability**:
- iOS 7.1+ - Deprecated in 14.0
- iPadOS 7.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
func contentItem(at indexPath: IndexPath) -> MPContentItem?
```

```objc
- (MPContentItem *) contentItemAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

The media item at the indicated index.

## Parameters

- `indexPath`: The index for the media item to be retrieved.

## See Also

### Retrieving a media item
- [func contentItem(forIdentifier: String, completionHandler: (MPContentItem?, (any Error)?) -> Void)](./contentitem%28foridentifier,completionhandler%29.md)
  Retrieves the content item associated with the provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/contentitem(at:))*