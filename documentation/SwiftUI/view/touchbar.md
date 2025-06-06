# touchBar(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func touchBar<Content>(_ touchBar: TouchBar<Content>) -> some View where Content : View
```

#### Return Value

A view that contains the Touch Bar content.

#### Discussion

Use [`touchBar(_:)`](view/touchbar(_:).md) to provide a static set of views that are displayed by the Touch Bar when appropriate, depending on whether the view has focus.

The example below provides Touch Bar content in-line, that creates the content the Touch Bar displays:

```swift
func selectHearts() {/* ... */ }
func selectClubs() { /* ... */ }
func selectSpades() { /* ... */ }
func selectDiamonds() { /* ... */ }

TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar {
        Button("♥️ - Hearts", action: selectHearts)
        Button("♣️ - Clubs", action: selectClubs)
        Button("♠️ - Spades", action: selectSpades)
        Button("♦️ - Diamonds", action: selectDiamonds)
    }
```

![A Touch Bar that shows content you create by using a static collection](https://docs-assets.developer.apple.com/published/50abda464413c0ca08d8e80cb02bce7b/SwiftUI-touchbar-static%402x.png)

## Parameters

- `touchBar`: A collection of views that the Touch Bar displays.

## See Also

- [func touchBar<Content>(content: () -> Content) -> some View](view/touchbar(content:).md)
  Sets the content that the Touch Bar displays.
- [func touchBarItemPrincipal(Bool) -> some View](view/touchbaritemprincipal(_:).md)
  Sets principal views that have special significance to this Touch Bar.
- [func touchBarCustomizationLabel(Text) -> some View](view/touchbarcustomizationlabel(_:).md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](view/touchbaritempresence(_:).md)
  Sets the behavior of the user-customized view.
- [struct TouchBar](touchbar.md)
  A container for a view that you can show in the Touch Bar.
- [enum TouchBarItemPresence](touchbaritempresence.md)
  Options that affect user customization of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/touchbar(_:))*