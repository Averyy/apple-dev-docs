# writeNDEF(_:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Saves an NDEF message to a writable tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeNDEF(_ ndefMessage: NFCNDEFMessage, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeNDEF(_ ndefMessage: NFCNDEFMessage) async throws
```

```objc
- (void) writeNDEF:(NFCNDEFMessage *) ndefMessage completionHandler:(void (^)(NSError *)) completionHandler;
```

#### Discussion

To determine whether the tag is writable, call [`queryNDEFStatus(completionHandler:)`](./queryndefstatus%28completionhandler%29.md) and check that the `status` is [`NFCNDEFStatus.readWrite`](../nfcndefstatus/readwrite.md).

## Parameters

- `ndefMessage`: The NDEF message to write to the tag.
- `completionHandler`: The handler invoked by the reader session after completing the write request. The session calls `completionHandler` on the dispatch queue provided when creating the [`NFCNDEFReaderSession`](../nfcndefreadersession.md).

  The handler has the following parameter:

  - **error**: An [`NSError`](../../Foundation/nserror.md) object if the write request fails. A value of `nil` indicates that the write was successful.

## See Also

### Writing to the Tag
- [func writeLock(completionHandler: ((any Error)?) -> Void)](./writelock%28completionhandler%29.md)
  Changes the NDEF tag status to read-only, preventing future write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/writendef(_:completionhandler:))*