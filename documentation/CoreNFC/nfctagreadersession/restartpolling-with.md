# restartPolling(with:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
func restartPolling(with configuration: NFCTagReaderSessionConfiguration)
```

#### Discussion

Restart the polling sequence in this session to discover new tags using the provided configuration.  New tags discovered from polling will return in the subsequent `[NFCTagReaderSessionDelegate tagReaderSession:didDetectTags:]` call. Tags that are returned previously by `[NFCTagReaderSessionDelegate tagReaderSession:didDetectTags:]` will become invalid, and all references to these tags shall be removed to properly release the resources.  Calling this method on an invalidated session will have no effect; a new reader session is required to restart the reader.

## Parameters

- `configuration`: Reader configuration used for the polling restart.  The configuration does not persist in the current active session, i.e.   would use   the original configuration from session instance initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/restartpolling(with:))*