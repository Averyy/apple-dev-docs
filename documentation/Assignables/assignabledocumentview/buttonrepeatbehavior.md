# buttonRepeatBehavior(_:)

**Framework**: Assignables  
**Kind**: method

Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func buttonRepeatBehavior(_ behavior: ButtonRepeatBehavior) -> some View
```

#### Discussion

Apply this to buttons that increment or decrement a value or perform some other inherently iterative operation. Interactions such as pressing-and-holding on the button, holding the button’s keyboard shortcut, or holding down the space key while the button is focused will trigger this repeat behavior.

```None
Button {
    playbackSpeed.advance(by: 1)
} label: {
    Label("Speed up", systemImage: "hare")
}
.buttonRepeatBehavior(.enabled)
```

This affects all system button styles, as well as automatically affects custom `ButtonStyle` conforming types. This does not automatically apply to custom `PrimitiveButtonStyle` conforming types, and the `EnvironmentValues.buttonRepeatBehavior` value should be used to adjust their custom gestures as appropriate.

## Parameters

- `behavior`: A value of   means that buttons should   enable repeating behavior and a value of   means that buttons   should disallow repeating behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/buttonrepeatbehavior(_:))*