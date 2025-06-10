# activateVoiceControlState(withIdentifier:)

**Framework**: CarPlay  
**Kind**: method

Changes the template’s state to the one matching the specified identifier.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func activateVoiceControlState(withIdentifier identifier: String)
```

#### Discussion

Your app must present the voice control template using its [`CPInterfaceController`](cpinterfacecontroller.md) object before the app can activate a new state. Calling this method before presenting the template has no effect on the active state.

> **Note**:  The voice control template applies a rate limit for voice control states, ignoring state changes occurring too rapidly or frequently in a short period of time.

## Parameters

- `identifier`: An identifier corresponding to one of the   associated with the template.

## See Also

- [var activeStateIdentifier: String?](cpvoicecontroltemplate/activestateidentifier.md)
  The identifier of the template’s current voice control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontroltemplate/activatevoicecontrolstate(withidentifier:))*