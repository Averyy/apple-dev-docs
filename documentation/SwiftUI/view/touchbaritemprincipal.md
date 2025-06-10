# touchBarItemPrincipal(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets principal views that have special significance to this Touch Bar.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func touchBarItemPrincipal(_ principal: Bool = true) -> some View
```

#### Return Value

A Touch Bar view with one element centered in the Touch Bar row.

#### Discussion

Use `touchBarItemPrincipal(_:)` to designate a view as a significant view in the Touch Bar. Currently, that view will be placed in the center of the row.

The example below sets the last button as the principal button for the Touch Bar view.

```swift
let touchBarItems = TouchBar(id: "myBarItems") {
    Button("♣️", action: {})
    Button("♥️", action: {})
    Button("♠️", action: {})
    Button("♦️", action: {})
       .touchBarItemPrincipal(true)
}

TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar(touchBarItems)
```

> **Note**: Multiple visible bars may each specify a principal view, but the system only honors one of them.

![A Touch Bar view showing one element designated as the principal view](https://docs-assets.developer.apple.com/published/ebd3f9fdec8875dcd3bb0da49e893ee7/SwiftUI-touchBarItemPrincipal%402x.png)

## Parameters

- `principal`: A Boolean value that indicates whether to display   this view prominently in the Touch Bar compared to other views.

## See Also

- [func touchBar<Content>(content: () -> Content) -> some View](view/touchbar(content:).md)
  Sets the content that the Touch Bar displays.
- [func touchBar<Content>(TouchBar<Content>) -> some View](view/touchbar(_:).md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBarCustomizationLabel(Text) -> some View](view/touchbarcustomizationlabel(_:).md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](view/touchbaritempresence(_:).md)
  Sets the behavior of the user-customized view.
- [struct TouchBar](touchbar.md)
  A container for a view that you can show in the Touch Bar.
- [enum TouchBarItemPresence](touchbaritempresence.md)
  Options that affect user customization of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/touchbaritemprincipal(_:))*