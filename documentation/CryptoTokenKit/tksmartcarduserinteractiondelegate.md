# TKSmartCardUserInteractionDelegate

**Framework**: CryptoTokenKit  
**Kind**: protocol  
**Role**: Protocol

The interface implemented by a Smart Card user interaction delegate to handle user interaction events.

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
protocol TKSmartCardUserInteractionDelegate
```

```objc
@protocol TKSmartCardUserInteractionDelegate
```

## Topics

### Delegate Methods
- [func characterEntered(in: TKSmartCardUserInteraction)](./tksmartcarduserinteractiondelegate/characterentered%28in%29.md)
  Tells the delegate that a valid character has been entered.
- [func correctionKeyPressed(in: TKSmartCardUserInteraction)](./tksmartcarduserinteractiondelegate/correctionkeypressed%28in%29.md)
  Tells the delegate that a correction key has been pressed.
- [func validationKeyPressed(in: TKSmartCardUserInteraction)](./tksmartcarduserinteractiondelegate/validationkeypressed%28in%29.md)
  Tells the delegate that the validation key has been pressed, indicating the end of PIN entry.
- [func invalidCharacterEntered(in: TKSmartCardUserInteraction)](./tksmartcarduserinteractiondelegate/invalidcharacterentered%28in%29.md)
  Tells the delegate that an invalid character has been entered.
- [func oldPINRequested(in: TKSmartCardUserInteraction)](./tksmartcarduserinteractiondelegate/oldpinrequested%28in%29.md)
  Tells the delegate that the old PIN needs to be entered.
- [func newPINRequested(in: TKSmartCardUserInteraction)](./tksmartcarduserinteractiondelegate/newpinrequested%28in%29.md)
  Tells the delegate that the new PIN needs to be entered.
- [func newPINConfirmationRequested(in: TKSmartCardUserInteraction)](./tksmartcarduserinteractiondelegate/newpinconfirmationrequested%28in%29.md)
  Tells the delegate that the new PIN needs to be re-entered for confirmation.

## See Also

### Handling User Interaction Events
- [var delegate: (any TKSmartCardUserInteractionDelegate)?](./tksmartcarduserinteraction/delegate.md)
  The delegate for observing events that occur during the user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate)*