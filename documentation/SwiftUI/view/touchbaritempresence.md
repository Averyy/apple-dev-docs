# touchBarItemPresence(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the behavior of the user-customized view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func touchBarItemPresence(_ presence: TouchBarItemPresence) -> some View
```

#### Return Value

A trait that describes the behavior for this Touch Bar view.

#### Discussion

Use `touchBarItemPresence(_:)` to define the visibility requirements of a particular Touch Bar view during customization by the user.

Touch Bar views may be:

- `.required`: not allowed to be removed by the user.
- `.default`: shown by default prior to user customization, but removable.
- `.optional`: not visible by default, but can be added through the customization palette.

Each [`TouchBarItemPresence`](touchbaritempresence.md) must be initialized with a string that is a globally unique identifier for this item.

In the example below, all of the Touch Bar items are visible in the Touch Bar by default, except for the “Clubs” item. It’s set to `.optional` but is configurable by the user:

```swift
TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar {
        Button("♥️", action: selectHearts)
            .touchBarItemPresence(.required("heartsKey"))
        Button("♣️", action: selectClubs)
            .touchBarItemPresence(.optional("clubsKey"))
        Button("♠️", action: selectSpades)
            .touchBarItemPresence(.required("spadesKey"))
        Button("♦️", action: selectDiamonds)
            .touchBarItemPresence(.required("diamondsKey"))
}
```

![A view showing the configuration of the Touch Bar with required and](https://docs-assets.developer.apple.com/published/39aa265ad81c120e7f2f5130bfcb3d08/SwiftUI-touchBarItemPresence%402x.png)

## Parameters

- `presence`: One of the allowed    descriptions.

## See Also

- [func touchBar<Content>(content: () -> Content) -> some View](view/touchbar(content:).md)
  Sets the content that the Touch Bar displays.
- [func touchBar<Content>(TouchBar<Content>) -> some View](view/touchbar(_:).md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBarItemPrincipal(Bool) -> some View](view/touchbaritemprincipal(_:).md)
  Sets principal views that have special significance to this Touch Bar.
- [func touchBarCustomizationLabel(Text) -> some View](view/touchbarcustomizationlabel(_:).md)
  Sets a user-visible string that identifies the view’s functionality.
- [struct TouchBar](touchbar.md)
  A container for a view that you can show in the Touch Bar.
- [enum TouchBarItemPresence](touchbaritempresence.md)
  Options that affect user customization of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/touchbaritempresence(_:))*