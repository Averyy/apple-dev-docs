# connect(to:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Connects the reader session to a tag and activates that tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func connect(to tag: any NFCNDEFTag, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func connect(to tag: any NFCNDEFTag) async throws
```

```objc
- (void) connectToTag:(id<NFCNDEFTag>) tag completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

A tag stays connected until your app connects to a different tag or restarts polling. Connecting to a tag that is already connected has no effect.

## Parameters

- `tag`: A tag that the reader session should attempt connecting to.
- `completionHandler`: A handler that the reader session invokes after completing the tag-connect request. The handler has the following parameter:

  - **error**: `nil` when the session successfully connects to the tag; otherwise, an [`NSError`](../../Foundation/nserror.md) object.

  The session calls `completionHandler` on the dispatch queue provided when creating the [`NFCNDEFReaderSession`](../nfcndefreadersession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersession/connect(to:completionhandler:))*