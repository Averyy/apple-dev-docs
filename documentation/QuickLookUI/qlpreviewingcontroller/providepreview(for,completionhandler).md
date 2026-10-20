# providePreview(for:completionHandler:)

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method

Prepares the preview of a file identified within a file preview request.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func providePreview(for request: QLFilePreviewRequest, completionHandler handler: @escaping @Sendable (QLPreviewReply?, (any Error)?) -> Void)
```

```swift
optional func providePreview(for request: QLFilePreviewRequest) async throws -> QLPreviewReply
```

```objc
- (void) providePreviewForFileRequest:(QLFilePreviewRequest *) request completionHandler:(void (^)(QLPreviewReply *reply, NSError *error)) handler;
```

## Parameters

- `request`: The file preview request that identifies the content to preview.
- `handler`: The closure to call with a https://developer.apple.com/documentation/quicklook/qlpreviewreply for the system to display as the preview.

## See Also

### Instance Methods
- [func preparePreviewOfFile(at: URL, completionHandler: ((any Error)?) -> Void)](./preparepreviewoffile%28at,completionhandler%29.md)
  Prepares the preview of a file at the specified file’s URL.
- [func preparePreviewOfSearchableItem(identifier: String, queryString: String?, completionHandler: ((any Error)?) -> Void)](./preparepreviewofsearchableitem%28identifier,querystring,completionhandler%29.md)
  Prepares the preview for a file by using the data from Spotlight’s searchable item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller/providepreview(for:completionhandler:))*