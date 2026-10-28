# NFCISO15693ReaderSession

**Framework**: Core NFC  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 11.0+ - Deprecated in 17.0
- iPadOS 11.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0

## Declaration

```objc
@interface NFCISO15693ReaderSession : NFCReaderSession
```

## Overview

Reader session for processing ISO15693 tags.  @link [NFCReaderSessionDelegate readerSession:didDetectTags:] @link/ will return tag objects that are conformed to the NFCISO15693Tag protocol.  This session requires the “com.apple.developer.nfc.readersession.formats” entitlement in your process.

NOTE: Only one NFCReaderSession can be active at any time in the system. Subsequent opened sessions will get queued up and processed by the system in FIFO order. The NFCISO15693 tag object returned by this session will only respond to the legacy APIs that are introduced in iOS11.

## Topics

### Instance Methods
- [- initWithDelegate:queue:](./nfciso15693readersession/initwithdelegate_queue_.md)
- [- restartPolling](./nfciso15693readersession/restartpolling.md)

## Relationships

### Inherits From
- [NFCReaderSession](./nfcreadersession-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693readersession)*