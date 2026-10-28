# NFCTagReaderSession.PollingOption

**Framework**: Core NFC  
**Kind**: struct  
**Role**: Structure

Options that determine the type of tags that a reader session should detect during a polling sequence.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

## Declaration

```swift
struct PollingOption
```

```c
enum NFCPollingOption : NSInteger;
```

## Overview

You can combine options to have the reader session scan and detect different tag types at the same time.

## Topics

### Polling Options
- [static var iso14443: NFCTagReaderSession.PollingOption](./pollingoption/iso14443.md)
  The option for detecting ISO 7816-compatible and MIFARE tags.
- [static var iso15693: NFCTagReaderSession.PollingOption](./pollingoption/iso15693.md)
  The option for detecting ISO 15693 tags.
- [static var iso18092: NFCTagReaderSession.PollingOption](./pollingoption/iso18092.md)
  The option for detecting FeliCa tags.
### Initializers
- [init(rawValue: Int)](./pollingoption/init%28rawvalue%29.md)
### Type Properties
- [static var pace: NFCTagReaderSession.PollingOption](./pollingoption/pace.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a Tag Reader Session
- [convenience init?(pollingOption: NFCTagReaderSession.PollingOption, delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue?)](./init%28pollingoption,delegate,queue%29.md)
  Creates an NFC tag reader session.
- [protocol NFCTagReaderSessionDelegate](../nfctagreadersessiondelegate-2joku.md)
  A protocol that an object implements to receive callbacks sent from an NFC tag reader session.
- [- initWithPollingOption:delegate:queue:](./initwithpollingoption_delegate_queue_.md)
  Intializes an NFC tag reader session.
- [NFCTagReaderSessionDelegate](../nfctagreadersessiondelegate-5gxiw.md)
  A protocol that an object implements to receive callbacks sent from an NFC tag reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/pollingoption)*