# NFCNDEFStatus

**Framework**: Core NFC  
**Kind**: enum

Constants that indicate status for an NDEF tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum NFCNDEFStatus
```

## Topics

### Statuses
- [NFCNDEFStatus.notSupported](nfcndefstatus/notsupported.md)
  A status indicating that that tag isn’t an NDEF-formatted tag.
- [NFCNDEFStatus.readOnly](nfcndefstatus/readonly.md)
  A status indicating that the tag supports reading NDEF message data only.
- [NFCNDEFStatus.readWrite](nfcndefstatus/readwrite.md)
  A status indicating that the tag supports reading and writing NDEF message data.
### Initializers
- [init?(rawValue: UInt)](nfcndefstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isAvailable: Bool](nfcndeftag/isavailable.md)
  A Boolean value that determines whether the NDEF tag is available in the current reader session.
- [func queryNDEFStatus(completionHandler: (NFCNDEFStatus, Int, (any Error)?) -> Void)](nfcndeftag/queryndefstatus(completionhandler:).md)
  Asks the reader session for the NDEF support status of the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefstatus)*