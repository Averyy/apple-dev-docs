# validationKeyPressed(in:)

**Framework**: CryptoTokenKit  
**Kind**: method

Tells the delegate that the validation key has been pressed, indicating the end of PIN entry.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func validationKeyPressed(in interaction: TKSmartCardUserInteraction)
```

## Parameters

- `interaction`: The user interaction.

## See Also

- [func characterEntered(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/characterentered(in:).md)
  Tells the delegate that a valid character has been entered.
- [func correctionKeyPressed(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/correctionkeypressed(in:).md)
  Tells the delegate that a correction key has been pressed.
- [func invalidCharacterEntered(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/invalidcharacterentered(in:).md)
  Tells the delegate that an invalid character has been entered.
- [func oldPINRequested(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/oldpinrequested(in:).md)
  Tells the delegate that the old PIN needs to be entered.
- [func newPINRequested(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/newpinrequested(in:).md)
  Tells the delegate that the new PIN needs to be entered.
- [func newPINConfirmationRequested(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/newpinconfirmationrequested(in:).md)
  Tells the delegate that the new PIN needs to be re-entered for confirmation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/validationkeypressed(in:))*