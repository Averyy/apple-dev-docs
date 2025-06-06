# tagReaderSession(_:didInvalidateWithError:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Tells the delegate the reason for invalidating a reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+

## Declaration

```swift
func tagReaderSession(_ session: NFCTagReaderSession, didInvalidateWithError error: any Error)
```

## Parameters

- `session`: The session that has become invalid. Your app should discard any references it has to this session.
- `error`: The error indicating the reason for invalidation of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersessiondelegate-2joku/tagreadersession(_:didinvalidatewitherror:))*