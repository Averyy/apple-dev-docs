# isConcatenated

**Framework**: Matter  
**Kind**: property

Whether this object represents a concatenated QR Code payload consisting of two or more underlying payloads. If YES, then:

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
var isConcatenated: Bool { get }
```

#### Discussion

- The constituent payloads are exposed in the `subPayloads` property.
- Properties other than `subPayloads` and `qrCodeString` (e.g. `vendorID`, `discriminator`) are not relevant to a concatenated payload and should not be used. If accessed, they will act as if the payload was not in fact concatenated, and return the relevant value associated with the first sub-payload. Mutating such a property will discard the additional sub-payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrsetuppayload/isconcatenated)*