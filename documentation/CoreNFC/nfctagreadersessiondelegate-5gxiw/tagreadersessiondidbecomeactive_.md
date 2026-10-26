# tagReaderSessionDidBecomeActive:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the reader session is active.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```objc
- (void) tagReaderSessionDidBecomeActive:(NFCTagReaderSession *) session;
```

#### Discussion

The reader session calls this method after the device begins scanning for new tags.

## Parameters

- `session`: The active reader session. Only one session can be active at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersessiondelegate-5gxiw/tagreadersessiondidbecomeactive:)*