# readerSession(_:didDetect:)

**Framework**: Core NFC  
**Kind**: method

Tells the delegate that the session detected NFC tags with NDEF messages and enables read-write capability for the session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func readerSession(_ session: NFCNDEFReaderSession, didDetect tags: [any NFCNDEFTag])
```

## See Also

- [func readerSession(NFCNDEFReaderSession, didDetectNDEFs: [NFCNDEFMessage])](nfcndefreadersessiondelegate/readersession(_:diddetectndefs:).md)
  Tells the delegate that the session detected NFC tags with NDEF messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersessiondelegate/readersession(_:diddetect:))*