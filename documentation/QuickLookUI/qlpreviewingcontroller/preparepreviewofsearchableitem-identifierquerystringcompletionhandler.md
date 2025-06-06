# preparePreviewOfSearchableItem(identifier:queryString:completionHandler:)

**Framework**: Quick Look UI  
**Kind**: method

Prepares the preview for a file by using the data from Spotlight’s searchable item.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func preparePreviewOfSearchableItem(identifier: String, queryString: String?) async throws
```

#### Discussion

The operating system calls this method only once from the main thread before it presents the previewing controller. To avoid blocking the main thread, don’t perform long-running or resource-intensive work.

## Parameters

- `identifier`: The identifier of the searchable item.
- `queryString`: A search string to associate with the searchable item.
- `handler`: A completion handler that notifies the platform that a preview is available. The operating system shows a loading spinner, so call the handler as soon as possible. You can call the completion handler asynchronously after returning from the callback.

## See Also

- [func preparePreviewOfFile(at: URL, completionHandler: ((any Error)?) -> Void)](qlpreviewingcontroller/preparepreviewoffile(at:completionhandler:).md)
  Prepares the preview of a file at the specified file’s URL.
- [func providePreview(for: QLFilePreviewRequest, completionHandler: (QLPreviewReply?, (any Error)?) -> Void)](qlpreviewingcontroller/providepreview(for:completionhandler:).md)
  Prepares the preview of a file identified within a file preview request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller/preparepreviewofsearchableitem(identifier:querystring:completionhandler:))*