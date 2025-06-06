# tagReaderSession(_:didDetect:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Tells the delegate that the session detected NFC tags.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+

## Declaration

```swift
func tagReaderSession(_ session: NFCTagReaderSession, didDetect tags: [NFCTag])
```

#### Discussion

The polling options specified when creating an [`NFCTagReaderSession`](nfctagreadersession.md) object determine the types of tags that the session can detect.

## Parameters

- `session`: The session that detected the tags.
- `tags`: An array of NFC tags detected by the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersessiondelegate-2joku/tagreadersession(_:diddetect:))*