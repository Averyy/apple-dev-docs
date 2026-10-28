# restartPolling

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+ - Deprecated in 17.0
- iPadOS 11.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0

## Declaration

```objc
- (void) restartPolling;
```

## Discussion

Restart the polling sequence in this session to discover new tags.  Tags that are returned previously by @link [NFCReaderSessionDelegate readerSession:didDetectTags:] @link/ will become invalid, and all references to these tags shall be removed to properly release the resources.  Calling this method on an invalidated session will have no effect; a new reader session is required to restart the reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693readersession/restartpolling)*