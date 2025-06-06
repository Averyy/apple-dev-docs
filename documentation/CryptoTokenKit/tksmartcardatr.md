# TKSmartCardATR

**Framework**: CryptoTokenKit  
**Kind**: class

A parsed ATR (Answer To Reset) message from a Smart Card.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class TKSmartCardATR
```

#### Overview

This class declares a programmatic interface to parsing an ATR from data or a byte stream, and accessing the individual parts.

> **Note**:  The [`TKSmartCardATR`](tksmartcardatr.md) class parses ATR messages according to the ISO/IEC 7816-3 specification.

 The [`TKSmartCardATR`](tksmartcardatr.md) class parses ATR messages according to the ISO/IEC 7816-3 specification.

## Topics

### Creating a Smart Card ATR
- [init?(bytes: Data)](tksmartcardatr/init(bytes:).md)
  Initializes a `TKSmartCardATR` object from a provided data object.
- [init?(source: () -> Int32)](tksmartcardatr/init(source:).md)
  Initializes a `TKSmartCardATR` object from a provided data source.
### Accessing ATR Attributes
- [var protocols: [NSNumber]](tksmartcardatr/protocols.md)
  An array of protocols indicated in the ATR
- [var bytes: Data](tksmartcardatr/bytes.md)
  The ATR message data.
- [var historicalBytes: Data](tksmartcardatr/historicalbytes.md)
  The ATR historical bytes, not including interface bytes or the TCK (check byte).
- [var historicalRecords: [TKCompactTLVRecord]?](tksmartcardatr/historicalrecords.md)
  A list of compact TLV records parsed from historical bytes.
### Retrieving Interface Groups
- [func interfaceGroup(at: Int) -> TKSmartCardATR.InterfaceGroup?](tksmartcardatr/interfacegroup(at:).md)
  Returns the interface group at the specified index.
- [func interfaceGroup(for: TKSmartCardProtocol) -> TKSmartCardATR.InterfaceGroup?](tksmartcardatr/interfacegroup(for:).md)
  Returns the interface group with the specified protocol.
- [TKSmartCardATR.InterfaceGroup](tksmartcardatr/interfacegroup.md)
  A single interface-bytes group for a Smart Card ATR (Answer to Reset).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var atr: TKSmartCardATR?](tksmartcardslot/atr.md)
  The ATR (Answer to Reset) of the inserted Smart Card, or `nil` if no Smart Card is inserted or the inserted Smart Card is mute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr)*