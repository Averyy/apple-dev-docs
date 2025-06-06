# init(pollingOption:delegate:queue:)

**Framework**: Core NFC  
**Kind**: init

Creates an NFC tag reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+

## Declaration

```swift
convenience init?(pollingOption: NFCTagReaderSession.PollingOption, delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue? = nil)
```

## Parameters

- `pollingOption`: One or more options specifying the type of tags that the reader session scans for and detects.
- `delegate`: An object that handles callbacks from the reader session.
- `queue`: A dispatch queue that the reader session uses when making callbacks to the delegate. When queue is  , the session creates and uses a serial dispatch queue.

## See Also

- [NFCTagReaderSession.PollingOption](nfctagreadersession/pollingoption.md)
  Options that determine the type of tags that a reader session should detect during a polling sequence.
- [protocol NFCTagReaderSessionDelegate](nfctagreadersessiondelegate-2joku.md)
  A protocol that an object implements to receive callbacks sent from an NFC tag reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/init(pollingoption:delegate:queue:))*