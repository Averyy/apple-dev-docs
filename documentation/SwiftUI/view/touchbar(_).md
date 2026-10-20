# touchBar(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

Use [`touchBar(_:)`](./touchbar%28_%29.md) to provide a static set of views that are displayed by the Touch Bar when appropriate, depending on whether the view has focus.

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

![A Touch Bar that shows content you create by using a static collection](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-touchbar-static@2x.png)

## Parameters

- `touchBar`: A collection of views that the Touch Bar displays.

## See Also

### Managing Touch Bar input
- [func touchBar<Content>(content: () -> Content) -> some View](./touchbar%28content%29.md)
  Sets the content that the Touch Bar displays.
- [func touchBarItemPrincipal(Bool) -> some View](./touchbaritemprincipal%28_%29.md)
  Sets principal views that have special significance to this Touch Bar.
- [func touchBarCustomizationLabel(Text) -> some View](./touchbarcustomizationlabel%28_%29.md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](./touchbaritempresence%28_%29.md)
  Sets the behavior of the user-customized view.
- [struct TouchBar](../touchbar.md)
  A container for a view that you can show in the Touch Bar.
- [enum TouchBarItemPresence](../touchbaritempresence.md)
  Options that affect user customization of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/touchbar(_:))*