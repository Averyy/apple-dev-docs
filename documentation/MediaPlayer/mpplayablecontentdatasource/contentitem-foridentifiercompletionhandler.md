# contentItem(forIdentifier:completionHandler:)

**Framework**: Media Player  
**Kind**: method

Retrieves the content item associated with the provided identifier.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func contentItem(forIdentifier identifier: String) async throws -> MPContentItem
```

#### Discussion

Client apps should always call the completion handler after loading has finished.

## Parameters

- `identifier`: The String that identifies a content item.
- `completionHandler`: A block that is called after the content item has been loaded.

## See Also

- [func contentItem(at: IndexPath) -> MPContentItem?](mpplayablecontentdatasource/contentitem(at:).md)
  Retrieves the media item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/contentitem(foridentifier:completionhandler:))*