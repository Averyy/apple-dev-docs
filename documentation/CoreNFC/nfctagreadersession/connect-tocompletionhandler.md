# connect(to:completionHandler:)

**Framework**: Core NFC  
**Kind**: method

Connects the reader session to a tag and activates that tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
func connect(to tag: NFCTag, completionHandler: @escaping ((any Error)?) -> Void)
```

#### Discussion

A tag stays connected until your app connects to a different tag or restarts polling. Connecting to a tag that is already connected has no effect.

## Parameters

- `tag`: A tag to which the reader session should attempt to connect.
- `completionHandler`: A handler that the reader session invokes after completing the tag-connect request. The handler has the following parameter: - **error**: `nil` when the session successfully connects to the tag; otherwise, an [`Error`](https://developer.apple.com/documentation/Swift/Error) object. The session calls `completionHandler` on the dispatch queue provided when creating the [`NFCTagReaderSession`](nfctagreadersession.md).

## See Also

- [var connectedTag: NFCTag?](nfctagreadersession/connectedtag-3mlqu.md)
  The tag connected to the reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/connect(to:completionhandler:))*