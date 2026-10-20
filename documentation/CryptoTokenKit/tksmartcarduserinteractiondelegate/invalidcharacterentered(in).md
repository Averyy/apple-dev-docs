# invalidCharacterEntered(in:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that an invalid character has been entered.

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
optional func invalidCharacterEntered(in interaction: TKSmartCardUserInteraction)
```

```objc
- (void) invalidCharacterEnteredInUserInteraction:(TKSmartCardUserInteraction *) interaction;
```

## Parameters

- `interaction`: The user interaction.

## See Also

### Delegate Methods
- [func characterEntered(in: TKSmartCardUserInteraction)](./characterentered%28in%29.md)
  Tells the delegate that a valid character has been entered.
- [func correctionKeyPressed(in: TKSmartCardUserInteraction)](./correctionkeypressed%28in%29.md)
  Tells the delegate that a correction key has been pressed.
- [func validationKeyPressed(in: TKSmartCardUserInteraction)](./validationkeypressed%28in%29.md)
  Tells the delegate that the validation key has been pressed, indicating the end of PIN entry.
- [func oldPINRequested(in: TKSmartCardUserInteraction)](./oldpinrequested%28in%29.md)
  Tells the delegate that the old PIN needs to be entered.
- [func newPINRequested(in: TKSmartCardUserInteraction)](./newpinrequested%28in%29.md)
  Tells the delegate that the new PIN needs to be entered.
- [func newPINConfirmationRequested(in: TKSmartCardUserInteraction)](./newpinconfirmationrequested%28in%29.md)
  Tells the delegate that the new PIN needs to be re-entered for confirmation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/invalidcharacterentered(in:))*