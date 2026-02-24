# init(configuration:delegate:queue:)

**Framework**: Core NFC  
**Kind**: init

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
init(configuration: NFCTagReaderSessionConfiguration, delegate: any __NFCTagReaderSessionDelegate, queue: dispatch_queue_t)
```

#### Return Value

A new NFCTagReaderSession instance.

## Parameters

- `configuration`: Reader configuration for the session.  The configuration is applied when `[NFCTagReaderSession beginSession]` or `[NFCTagReaderSession restartPolling]` is called.
- `delegate`: The session will hold a weak ARC reference to this `NFCTagReaderSessionDelegate` object.
- `queue`: A dispatch queue where NFCTagReaderSessionDelegate delegate callbacks will be dispatched to.  A nil value will cause the creation of a serial dispatch queue internally for the session.  The session object will retain the provided dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/init(configuration:delegate:queue:)-8g6tm)*