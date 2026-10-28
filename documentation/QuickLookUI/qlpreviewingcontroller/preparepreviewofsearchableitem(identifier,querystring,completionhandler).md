# preparePreviewOfSearchableItem(identifier:queryString:completionHandler:)

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method

Prepares the preview for a file by using the data from Spotlight’s searchable item.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func preparePreviewOfSearchableItem(identifier: String, queryString: String?, completionHandler handler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
optional func preparePreviewOfSearchableItem(identifier: String, queryString: String?) async throws
```

```objc
- (void) preparePreviewOfSearchableItemWithIdentifier:(NSString *) identifier queryString:(NSString *) queryString completionHandler:(void (^)(NSError *)) handler;
```

## Discussion

The operating system calls this method only once from the main thread before it presents the previewing controller. To avoid blocking the main thread, don’t perform long-running or resource-intensive work.

## Parameters

- `identifier`: The identifier of the searchable item.
- `queryString`: A search string to associate with the searchable item.
- `handler`: A completion handler that notifies the platform that a preview is available. The operating system shows a loading spinner, so call the handler as soon as possible. You can call the completion handler asynchronously after returning from the callback.

## See Also

### Instance Methods
- [func preparePreviewOfFile(at: URL, completionHandler: ((any Error)?) -> Void)](./preparepreviewoffile%28at,completionhandler%29.md)
  Prepares the preview of a file at the specified file’s URL.
- [func providePreview(for: QLFilePreviewRequest, completionHandler: (QLPreviewReply?, (any Error)?) -> Void)](./providepreview%28for,completionhandler%29.md)
  Prepares the preview of a file identified within a file preview request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller/preparepreviewofsearchableitem(identifier:querystring:completionhandler:))*