# touchBarCustomizationLabel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

![A Touch Bar customization view showing labels assigned to the Touch](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-touchBarCustomizationLabel@2x.png)

## Parameters

- `label`: A `Text` view containing the customization label.

## See Also

### Managing Touch Bar input
- [func touchBar<Content>(content: () -> Content) -> some View](./touchbar%28content%29.md)
  Sets the content that the Touch Bar displays.
- [func touchBar<Content>(TouchBar<Content>) -> some View](./touchbar%28_%29.md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBarItemPrincipal(Bool) -> some View](./touchbaritemprincipal%28_%29.md)
  Sets principal views that have special significance to this Touch Bar.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](./touchbaritempresence%28_%29.md)
  Sets the behavior of the user-customized view.
- [struct TouchBar](../touchbar.md)
  A container for a view that you can show in the Touch Bar.
- [enum TouchBarItemPresence](../touchbaritempresence.md)
  Options that affect user customization of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/touchbarcustomizationlabel(_:))*