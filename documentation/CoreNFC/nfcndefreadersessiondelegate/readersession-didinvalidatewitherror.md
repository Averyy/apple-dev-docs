# readerSession(_:didInvalidateWithError:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Tells the delegate the reason for invalidating a reader session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readerSession(_ session: NFCNDEFReaderSession, didInvalidateWithError error: any Error)
```

## Parameters

- `session`: The session that has become invalid. Your app should discard any references it has to this session.
- `error`: The error indicating the reason for invalidation of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersessiondelegate/readersession(_:didinvalidatewitherror:))*