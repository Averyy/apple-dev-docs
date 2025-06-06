# restartPolling()

**Framework**: Core NFC  
**Kind**: method

Restarts the polling sequence so the reader session can discover new tags.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func restartPolling()
```

#### Discussion

After restarting the polling sequence, the reader session sends newly detected tags to the session’s delegate method [`tagReaderSession(_:didDetect:)`](nfctagreadersessiondelegate-2joku/tagreadersession(_:diddetect:).md).

> **Note**:  Tags detected before polling restarts are invalid. Your app should discard any references it has to the invalid tags to free system resources.

 Tags detected before polling restarts are invalid. Your app should discard any references it has to the invalid tags to free system resources.

Calling [`restartPolling()`](nfctagreadersession/restartpolling().md) on an invalidated session has no effect. If you need to restart the reader session, create a new [`NFCTagReaderSession`](nfctagreadersession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/restartpolling())*