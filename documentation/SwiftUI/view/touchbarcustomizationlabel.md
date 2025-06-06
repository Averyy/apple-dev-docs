# touchBarCustomizationLabel(_:)

**Framework**: SwiftUI  
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

![A Touch Bar customization view showing labels assigned to the Touch](https://docs-assets.developer.apple.com/published/cdb67ec595f9e8587676a192396b6286/SwiftUI-touchBarCustomizationLabel%402x.png)

## Parameters

- `label`: A   view containing the customization label.

## See Also

- [func touchBar<Content>(content: () -> Content) -> some View](view/touchbar(content:).md)
  Sets the content that the Touch Bar displays.
- [func touchBar<Content>(TouchBar<Content>) -> some View](view/touchbar(_:).md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBarItemPrincipal(Bool) -> some View](view/touchbaritemprincipal(_:).md)
  Sets principal views that have special significance to this Touch Bar.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](view/touchbaritempresence(_:).md)
  Sets the behavior of the user-customized view.
- [struct TouchBar](touchbar.md)
  A container for a view that you can show in the Touch Bar.
- [enum TouchBarItemPresence](touchbaritempresence.md)
  Options that affect user customization of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/touchbarcustomizationlabel(_:))*