# contentItem(forIdentifier:completionHandler:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Retrieves the content item associated with the provided identifier.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
optional func contentItem(forIdentifier identifier: String, completionHandler: @escaping @Sendable (MPContentItem?, (any Error)?) -> Void)
```

```swift
optional func contentItem(forIdentifier identifier: String) async throws -> MPContentItem
```

```objc
- (void) contentItemForIdentifier:(NSString *) identifier completionHandler:(void (^)(MPContentItem *, NSError *)) completionHandler;
```

#### Discussion

Client apps should always call the completion handler after loading has finished.

## Parameters

- `identifier`: The String that identifies a content item.
- `completionHandler`: A block that is called after the content item has been loaded.

  - **contentItem**: The content item associated with the identifier. If there is no content item, the value of this parameter is `nil`.
  - **error**: If an error occurred, this parameter holds the error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

### Retrieving a media item
- [func contentItem(at: IndexPath) -> MPContentItem?](./contentitem%28at%29.md)
  Retrieves the media item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/contentitem(foridentifier:completionhandler:))*