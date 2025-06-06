# touchBarCustomizationLabel(_:)

**Framework**: MusicKit  
**Kind**: method

Sets a user-visible string that identifies the view’s functionality.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func touchBarCustomizationLabel(_ label: Text) -> some View
```

#### Return Value

A Touch Bar element with a set customization label.

#### Discussion

This string is visible during user customization.

```swift
TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar {
        Button("♥️", action: selectHearts)
            .touchBarCustomizationLabel(Text("Hearts"))
        Button("♣️", action: selectClubs)
            .touchBarCustomizationLabel(Text("Clubs"))
        Button("♠️", action: selectSpades)
            .touchBarCustomizationLabel(Text("Spades"))
        Button("♦️", action: selectDiamonds)
            .touchBarCustomizationLabel(Text("Diamonds"))
    }
```

## Parameters

- `label`: A   view containing the customization label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/touchbarcustomizationlabel(_:))*