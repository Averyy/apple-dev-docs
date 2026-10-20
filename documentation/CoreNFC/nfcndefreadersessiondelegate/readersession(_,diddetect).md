# readerSession(_:didDetect:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the session detected NFC tags with NDEF messages and enables read-write capability for the session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func readerSession(_ session: NFCNDEFReaderSession, didDetect tags: [any NFCNDEFTag])
```

```objc
- (void) readerSession:(NFCNDEFReaderSession *) session didDetectTags:(NSArray<__kindof id<NFCNDEFTag>> *) tags;
```

## See Also

### Finding NDEF Messages and Tags
- [func readerSession(NFCNDEFReaderSession, didDetectNDEFs: [NFCNDEFMessage])](./readersession%28_,diddetectndefs%29.md)
  Tells the delegate that the session detected NFC tags with NDEF messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersessiondelegate/readersession(_:diddetect:))*