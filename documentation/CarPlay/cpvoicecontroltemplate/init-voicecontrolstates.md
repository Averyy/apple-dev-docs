# init(voiceControlStates:)

**Framework**: CarPlay  
**Kind**: init

Creates a voice control template with a list of voice control states.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(voiceControlStates: [CPVoiceControlState])
```

#### Return Value

A newly initialized voice control template.

#### Discussion

When presenting the voice control template for the first time, the template defaults to the first state in the `voiceControlStates` array. You can change the state after presenting the template by calling the [`activateVoiceControlState(withIdentifier:)`](cpvoicecontroltemplate/activatevoicecontrolstate(withidentifier:).md) method.

## Parameters

- `voiceControlStates`: An array of voice control states associated with the template. You can provide up to five states. If you provide more, the template ignores any states after the first five in the array.

## See Also

- [class CPVoiceControlState](cpvoicecontrolstate.md)
  A voice control state containing title variants and images for use by a voice control template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontroltemplate/init(voicecontrolstates:))*