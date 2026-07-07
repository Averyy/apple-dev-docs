# restartPolling(configuration:)

**Framework**: Core NFC  
**Kind**: method

Restart the polling sequence in this session to discover new tags using the provided configuration.  New tags discovered from polling will return in the subsequent `NFCTagReaderSessionDelegate.tagReaderSession(_:, didDetect:)` call. Tags that are returned previously by `NFCTagReaderSessionDelegate.tagReaderSession(_:, didDetect:)` will become invalid, and all references to these tags shall be removed to properly release the resources. Calling this method on an invalidated session will have no effect; a new reader session is required to restart the reader.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func restartPolling(configuration: NFCTagReaderSession.Configuration)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/restartpolling(configuration:))*