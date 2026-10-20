# readerSession(_:didInvalidateWithError:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the session become invalid and provides the reason.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readerSession(_ session: NFCVASReaderSession, didInvalidateWithError error: any Error)
```

```objc
- (void) readerSession:(NFCVASReaderSession *) session didInvalidateWithError:(NSError *) error;
```

#### Discussion

Your app should release any references it has to the reader session that called this method.

## Parameters

- `session`: The reader session that calls this method.
- `error`: The error indicating the reason for invalidating the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasreadersessiondelegate/readersession(_:didinvalidatewitherror:))*