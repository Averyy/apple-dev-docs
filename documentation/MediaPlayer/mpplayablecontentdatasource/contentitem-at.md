# contentItem(at:)

**Framework**: Media Player  
**Kind**: method  
**Required**: Yes

Retrieves the media item at the specified index.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func contentItem(at indexPath: IndexPath) -> MPContentItem?
```

#### Return Value

The media item at the indicated index.

## Parameters

- `indexPath`: The index for the media item to be retrieved.

## See Also

- [func contentItem(forIdentifier: String, completionHandler: (MPContentItem?, (any Error)?) -> Void)](mpplayablecontentdatasource/contentitem(foridentifier:completionhandler:).md)
  Retrieves the content item associated with the provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/contentitem(at:))*