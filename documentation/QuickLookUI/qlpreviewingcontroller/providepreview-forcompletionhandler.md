# providePreview(for:completionHandler:)

**Framework**: Quick Look UI  
**Kind**: method

Prepares the preview of a file identified within a file preview request.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func providePreview(for request: QLFilePreviewRequest) async throws -> QLPreviewReply
```

## Parameters

- `request`: The file preview request that identifies the content to preview.
- `handler`: The closure to call with a doc://com.apple.documentation/documentation/quicklook/qlpreviewreply for the system to display as the preview.

## See Also

- [func preparePreviewOfFile(at: URL, completionHandler: ((any Error)?) -> Void)](qlpreviewingcontroller/preparepreviewoffile(at:completionhandler:).md)
  Prepares the preview of a file at the specified file’s URL.
- [func preparePreviewOfSearchableItem(identifier: String, queryString: String?, completionHandler: ((any Error)?) -> Void)](qlpreviewingcontroller/preparepreviewofsearchableitem(identifier:querystring:completionhandler:).md)
  Prepares the preview for a file by using the data from Spotlight’s searchable item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller/providepreview(for:completionhandler:))*