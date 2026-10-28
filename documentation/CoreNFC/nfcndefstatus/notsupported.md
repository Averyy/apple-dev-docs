# NFCNDEFStatus.notSupported

**Framework**: Core NFC  
**Kind**: case  
**Role**: Case

A status indicating that that tag isn’t an NDEF-formatted tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case notSupported
```

```c
NFCNDEFStatusNotSupported
```

## Discussion

You cannot perform read and write operations on the tag.

## See Also

### Statuses
- [NFCNDEFStatus.readOnly](./readonly.md)
  A status indicating that the tag supports reading NDEF message data only.
- [NFCNDEFStatus.readWrite](./readwrite.md)
  A status indicating that the tag supports reading and writing NDEF message data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefstatus/notsupported)*