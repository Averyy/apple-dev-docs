# NFCTagReaderSession.PollingOption

**Framework**: Core NFC  
**Kind**: struct

Options that determine the type of tags that a reader session should detect during a polling sequence.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
struct PollingOption
```

#### Overview

You can combine options to have the reader session scan and detect different tag types at the same time.

## Topics

### Polling Options
- [static var iso14443: NFCTagReaderSession.PollingOption](nfctagreadersession/pollingoption/iso14443.md)
  The option for detecting ISO 7816-compatible and MIFARE tags.
- [static var iso15693: NFCTagReaderSession.PollingOption](nfctagreadersession/pollingoption/iso15693.md)
  The option for detecting ISO 15693 tags.
- [static var iso18092: NFCTagReaderSession.PollingOption](nfctagreadersession/pollingoption/iso18092.md)
  The option for detecting FeliCa tags.
### Initializers
- [init(rawValue: Int)](nfctagreadersession/pollingoption/init(rawvalue:).md)
### Type Properties
- [static var pace: NFCTagReaderSession.PollingOption](nfctagreadersession/pollingoption/pace.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [convenience init?(pollingOption: NFCTagReaderSession.PollingOption, delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue?)](nfctagreadersession/init(pollingoption:delegate:queue:).md)
  Creates an NFC tag reader session.
- [protocol NFCTagReaderSessionDelegate](nfctagreadersessiondelegate-2joku.md)
  A protocol that an object implements to receive callbacks sent from an NFC tag reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/pollingoption)*