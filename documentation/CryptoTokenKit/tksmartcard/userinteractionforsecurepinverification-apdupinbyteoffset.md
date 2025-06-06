# userInteractionForSecurePINVerification(_:apdu:pinByteOffset:)

**Framework**: CryptoTokenKit  
**Kind**: method

Creates and returns a new user interaction object for secure PIN verification using the Smart Card reader facilities.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func userInteractionForSecurePINVerification(_ PINFormat: TKSmartCardPINFormat, apdu APDU: Data, pinByteOffset PINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?
```

#### Return Value

A new user interaction object for secure PIN verification, or `nil` if this feature is not supported by the Smart Card reader.

#### Discussion

You should only call this method after a session to the Smart Card has been established using the [`beginSession(reply:)`](tksmartcard/beginsession(reply:).md) method, and before the session is terminated using the [`endSession()`](tksmartcard/endsession().md) method.

Once the interaction has been successfully completed, the results are available via the [`resultData`](tksmartcarduserinteractionforpinoperation/resultdata.md) and [`resultSW`](tksmartcarduserinteractionforpinoperation/resultsw.md) properties of the returned [`TKSmartCardUserInteractionForSecurePINVerification`](tksmartcarduserinteractionforsecurepinverification.md) object.

## Parameters

- `PINFormat`: The PIN format descriptor.
- `APDU`: The Application Protocol Data Unit (APDU) used by the Smart Card to fill in PIN data.
- `PINByteOffset`: The offset, in bytes, within the Application Protocol Data Unit (APDU) field to mark a location of a PIN block for filling in the entered PIN.

## See Also

- [func userInteractionForSecurePINChange(TKSmartCardPINFormat, apdu: Data, currentPINByteOffset: Int, newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange?](tksmartcard/userinteractionforsecurepinchange(_:apdu:currentpinbyteoffset:newpinbyteoffset:).md)
  Creates a new user interaction object for secure PIN change using the smart card reader facilities (typically a HW keypad).
- [class TKSmartCardPINFormat](tksmartcardpinformat.md)
  The formatting properties for a PIN, such as character encoding and length constraints.
- [class TKSmartCardUserInteraction](tksmartcarduserinteraction.md)
  The base class for encapsulating user interaction with a Smart Card reader.
- [class TKSmartCardUserInteractionForPINOperation](tksmartcarduserinteractionforpinoperation.md)
  A representation of user interaction for secure PIN operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINChange](tksmartcarduserinteractionforsecurepinchange.md)
  A representation of the user interaction for secure PIN change operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINVerification](tksmartcarduserinteractionforsecurepinverification.md)
  A representation of the user interaction for secure PIN change verification on a Smart Card reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/userinteractionforsecurepinverification(_:apdu:pinbyteoffset:))*