# preparePreviewOfFile(at:completionHandler:)

**Framework**: Quick Look UI  
**Kind**: method

Prepares the preview of a file at the specified file’s URL.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func preparePreviewOfFile(at url: URL) async throws
```

#### Discussion

The operating system calls this method only once from the main thread before it presents the previewing controller. To avoid blocking the main thread, don’t perform long-running or resource-intensive work.

When preparing and displaying the view controller, avoid holding open a file descriptors while the user is previewing the file.

## Parameters

- `url`: The URL of the file to preview.
- `handler`: A completion handler that notifies the platform that a preview is available. The operating system shows a loading spinner, so call the handler as soon as possible. You can call the completion handler asynchronously after returning from the callback.

## See Also

- [func preparePreviewOfSearchableItem(identifier: String, queryString: String?, completionHandler: ((any Error)?) -> Void)](qlpreviewingcontroller/preparepreviewofsearchableitem(identifier:querystring:completionhandler:).md)
  Prepares the preview for a file by using the data from Spotlight’s searchable item.
- [func providePreview(for: QLFilePreviewRequest, completionHandler: (QLPreviewReply?, (any Error)?) -> Void)](qlpreviewingcontroller/providepreview(for:completionhandler:).md)
  Prepares the preview of a file identified within a file preview request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller/preparepreviewoffile(at:completionhandler:))*