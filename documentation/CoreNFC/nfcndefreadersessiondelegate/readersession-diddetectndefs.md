# readerSession(_:didDetectNDEFs:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Tells the delegate that the session detected NFC tags with NDEF messages.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readerSession(_ session: NFCNDEFReaderSession, didDetectNDEFs messages: [NFCNDEFMessage])
```

#### Discussion

The reader session calls this method when it detects NFC tags with NDEF messages in the polling sequence. The session restarts polling when the detected tags are no longer within reading range of the iOS device.

> ❗ **Important**:  The reader session doesn’t call this method when the delegate provides the [`readerSession(_:didDetect:)`](nfcndefreadersessiondelegate/readersession(_:diddetect:).md) method.

## Parameters

- `session`: The reader session calling this method.
- `messages`: An array of the NDEF messages in the order they were discovered on the tag.

## See Also

- [func readerSession(NFCNDEFReaderSession, didDetect: [any NFCNDEFTag])](nfcndefreadersessiondelegate/readersession(_:diddetect:).md)
  Tells the delegate that the session detected NFC tags with NDEF messages and enables read-write capability for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersessiondelegate/readersession(_:diddetectndefs:))*