# readerSessionDidBecomeActive(_:)

**Framework**: Core NFC  
**Kind**: method

Tells the delegate that the reader session is active.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func readerSessionDidBecomeActive(_ session: NFCVASReaderSession)
```

#### Discussion

The reader session calls this method after the device begins scanning for new tags.

## Parameters

- `session`: The active reader session. Only one session can be active at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasreadersessiondelegate/readersessiondidbecomeactive(_:))*