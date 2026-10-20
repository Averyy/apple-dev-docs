# queryNDEFStatus(completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the reader session for the NDEF support status of the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func queryNDEFStatus(completionHandler: @escaping @Sendable (NFCNDEFStatus, Int, (any Error)?) -> Void)
```

```swift
func queryNDEFStatus() async throws -> (NFCNDEFStatus, Int)
```

```objc
- (void) queryNDEFStatusWithCompletionHandler:(void (^)(NFCNDEFStatus status, NSUInteger capacity, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: The handler invoked by the reader session that provides the NDEF support status. The handler has the following parameters:

  - **status**: The [`NFCNDEFStatus`](../nfcndefstatus.md) of the tag.
  - **capacity**: Indicates the maximum NDEF message size, in bytes, that you can store on the tag.
  - **error**: An [`NSError`](../../Foundation/nserror.md) object if the query fails; otherwise, `nil`.

  The session calls `completionHandler` on the dispatch queue provided when creating the [`NFCNDEFReaderSession`](../nfcndefreadersession.md).

## See Also

### Getting the Tag Status
- [var isAvailable: Bool](./isavailable.md)
  A Boolean value that determines whether the NDEF tag is available in the current reader session.
- [enum NFCNDEFStatus](../nfcndefstatus.md)
  Constants that indicate status for an NDEF tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/queryndefstatus(completionhandler:))*