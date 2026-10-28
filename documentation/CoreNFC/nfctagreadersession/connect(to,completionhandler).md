# connect(to:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Connects the reader session to a tag and activates that tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
@preconcurrency
func connect(to tag: NFCTag, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

## Discussion

A tag stays connected until your app connects to a different tag or restarts polling. Connecting to a tag that is already connected has no effect.

## Parameters

- `tag`: A tag to which the reader session should attempt to connect.
- `completionHandler`: A handler that the reader session invokes after completing the tag-connect request. The handler has the following parameter:

  - **error**: `nil` when the session successfully connects to the tag; otherwise, an [`Error`](../../Swift/error.md) object.

  The session calls `completionHandler` on the dispatch queue provided when creating the [`NFCTagReaderSession`](../nfctagreadersession.md).

## See Also

### Connecting to a Tag
- [var connectedTag: NFCTag?](./connectedtag-3mlqu.md)
  The tag connected to the reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/connect(to:completionhandler:))*