# readNDEF(completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Retrieves an NDEF message from the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readNDEF(completionHandler: @escaping @Sendable (NFCNDEFMessage?, (any Error)?) -> Void)
```

```swift
func readNDEF() async throws -> NFCNDEFMessage
```

```objc
- (void) readNDEFWithCompletionHandler:(void (^)(NFCNDEFMessage *, NSError *)) completionHandler;
```

## Parameters

- `completionHandler`: The handler invoked by the reader session that provides the NDEF message. The handler has the following parameters:

  - **message**: An [`NFCNDEFMessage`](../nfcndefmessage.md) object, or `nil` if an error occurs while retrieving the message.
  - **error**: An [`NSError`](../../Foundation/nserror.md) object if the read request fails; otherwise, `nil`.

  The session calls `completionHandler` on the dispatch queue provided when creating the [`NFCNDEFReaderSession`](../nfcndefreadersession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/readndef(completionhandler:))*