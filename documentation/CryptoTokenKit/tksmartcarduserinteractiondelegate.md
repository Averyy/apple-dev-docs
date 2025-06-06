# TKSmartCardUserInteractionDelegate

**Framework**: CryptoTokenKit  
**Kind**: protocol

The interface implemented by a Smart Card user interaction delegate to handle user interaction events.

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
protocol TKSmartCardUserInteractionDelegate
```

## Topics

### Delegate Methods
- [func characterEntered(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/characterentered(in:).md)
  Tells the delegate that a valid character has been entered.
- [func correctionKeyPressed(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/correctionkeypressed(in:).md)
  Tells the delegate that a correction key has been pressed.
- [func validationKeyPressed(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/validationkeypressed(in:).md)
  Tells the delegate that the validation key has been pressed, indicating the end of PIN entry.
- [func invalidCharacterEntered(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/invalidcharacterentered(in:).md)
  Tells the delegate that an invalid character has been entered.
- [func oldPINRequested(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/oldpinrequested(in:).md)
  Tells the delegate that the old PIN needs to be entered.
- [func newPINRequested(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/newpinrequested(in:).md)
  Tells the delegate that the new PIN needs to be entered.
- [func newPINConfirmationRequested(in: TKSmartCardUserInteraction)](tksmartcarduserinteractiondelegate/newpinconfirmationrequested(in:).md)
  Tells the delegate that the new PIN needs to be re-entered for confirmation.

## See Also

- [var delegate: (any TKSmartCardUserInteractionDelegate)?](tksmartcarduserinteraction/delegate.md)
  The delegate for observing events that occur during the user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate)*