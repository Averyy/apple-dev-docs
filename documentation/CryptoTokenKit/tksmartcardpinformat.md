# TKSmartCardPINFormat

**Framework**: CryptoTokenKit  
**Kind**: class

The formatting properties for a PIN, such as character encoding and length constraints.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class TKSmartCardPINFormat
```

#### Overview

You typically interact with `TKSmartCardPINFormat` objects when calling the [`userInteractionForSecurePINChange(_:apdu:currentPINByteOffset:newPINByteOffset:)`](tksmartcard/userinteractionforsecurepinchange(_:apdu:currentpinbyteoffset:newpinbyteoffset:).md) and [`userInteractionForSecurePINVerification(_:apdu:pinByteOffset:)`](tksmartcard/userinteractionforsecurepinverification(_:apdu:pinbyteoffset:).md) methods on an instance of [`TKSmartCard`](tksmartcard.md).

## Topics

### Configuring PIN Formatting
- [var charset: TKSmartCardPINFormat.Charset](tksmartcardpinformat/charset-swift.property.md)
  The format of PIN characters. `TKSmartCardPINCharsetNumeric` by default.
- [var encoding: TKSmartCardPINFormat.Encoding](tksmartcardpinformat/encoding-swift.property.md)
  The encoding of PIN characters. `TKSmartCardPINEncodingASCII` by default.
- [var minPINLength: Int](tksmartcardpinformat/minpinlength.md)
  The minimum number of characters to form a valid PIN. `4` by default.
- [var maxPINLength: Int](tksmartcardpinformat/maxpinlength.md)
  The maximum number of characters to form a valid PIN. `8` by default.
- [var pinBlockByteLength: Int](tksmartcardpinformat/pinblockbytelength.md)
  The total length of the PIN block in bytes. `8` by default.
- [var pinJustification: TKSmartCardPINFormat.Justification](tksmartcardpinformat/pinjustification.md)
  The justification within the PIN block. `TKSmartCardPINJustificationLeft` by default.
- [var pinBitOffset: Int](tksmartcardpinformat/pinbitoffset.md)
  The offset, in bits, within the PIN block to mark a location for filling in the formatted PIN, which is justified with respect to the [`pinJustification`](tksmartcardpinformat/pinjustification.md) property value. `0` by default.
- [var pinLengthBitOffset: Int](tksmartcardpinformat/pinlengthbitoffset.md)
  The offset, in bits, within the PIN block to mark a location for filling in the PIN length, which is always left justified. `0` by default.
- [var pinLengthBitSize: Int](tksmartcardpinformat/pinlengthbitsize.md)
  The size, in bits, of the PIN length field. If set to `0`, PIN length is not written. `0` by default.
### PIN Characteristics
- [TKSmartCardPINFormat.Charset](tksmartcardpinformat/charset-swift.enum.md)
  Possible PIN character sets.
- [TKSmartCardPINFormat.Encoding](tksmartcardpinformat/encoding-swift.enum.md)
  Possible PIN encoding types.
- [TKSmartCardPINFormat.Justification](tksmartcardpinformat/justification.md)
  Possible PIN justification types

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

- [func userInteractionForSecurePINVerification(TKSmartCardPINFormat, apdu: Data, pinByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?](tksmartcard/userinteractionforsecurepinverification(_:apdu:pinbyteoffset:).md)
  Creates and returns a new user interaction object for secure PIN verification using the Smart Card reader facilities.
- [func userInteractionForSecurePINChange(TKSmartCardPINFormat, apdu: Data, currentPINByteOffset: Int, newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange?](tksmartcard/userinteractionforsecurepinchange(_:apdu:currentpinbyteoffset:newpinbyteoffset:).md)
  Creates a new user interaction object for secure PIN change using the smart card reader facilities (typically a HW keypad).
- [class TKSmartCardUserInteraction](tksmartcarduserinteraction.md)
  The base class for encapsulating user interaction with a Smart Card reader.
- [class TKSmartCardUserInteractionForPINOperation](tksmartcarduserinteractionforpinoperation.md)
  A representation of user interaction for secure PIN operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINChange](tksmartcarduserinteractionforsecurepinchange.md)
  A representation of the user interaction for secure PIN change operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINVerification](tksmartcarduserinteractionforsecurepinverification.md)
  A representation of the user interaction for secure PIN change verification on a Smart Card reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat)*