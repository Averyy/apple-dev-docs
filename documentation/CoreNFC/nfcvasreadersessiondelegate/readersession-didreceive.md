# readerSession(_:didReceive:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Tells the delegate that the reader session received a VAS response.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readerSession(_ session: NFCVASReaderSession, didReceive responses: [NFCVASResponse])
```

#### Discussion

The reader session restarts polling when the detected tag moves from the session’s read range.

## Parameters

- `session`: The reader session that calls this method.
- `responses`: An array of   objects. The order of the response objects follows the sequence of   sent to the tag by the reader session.

## See Also

- [class NFCVASResponse](nfcvasresponse.md)
  An object representing the response from a single `GET VAS DATA` command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasreadersessiondelegate/readersession(_:didreceive:))*