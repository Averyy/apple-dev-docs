# isAvailable

**Framework**: Core NFC  
**Kind**: property  
**Required**: Yes

A Boolean value that determines whether the NDEF tag is available in the current reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isAvailable: Bool { get }
```

#### Discussion

A tag removed from the RF field becomes unavailable, and a tag in a disconnected state is also unavailable.

## See Also

- [func queryNDEFStatus(completionHandler: (NFCNDEFStatus, Int, (any Error)?) -> Void)](nfcndeftag/queryndefstatus(completionhandler:).md)
  Asks the reader session for the NDEF support status of the tag.
- [enum NFCNDEFStatus](nfcndefstatus.md)
  Constants that indicate status for an NDEF tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/isavailable)*