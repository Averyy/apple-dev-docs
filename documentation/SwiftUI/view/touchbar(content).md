# touchBar(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the content that the Touch Bar displays.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func touchBar<Content>(@ContentBuilder content: () -> Content) -> some View where Content : View
```

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` when you need to dynamically construct items to show in the Touch Bar. The content is displayed by the Touch Bar when appropriate, depending on focus.

In the example below, four buttons are added to a Touch Bar content struct and then added to the Touch Bar:

```swift
let touchBarItems = TouchBar(id: "myBarItems") {
    Button("♣️", action: {})
    Button("♥️", action: {})
    Button("♠️", action: {})
    Button("♦️", action: {})
}

TextField("TouchBar Demo", text: $placeholder)
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .focusable()
    .touchBar(touchBarItems)
```

![A Touch Bar that shows content you create using a Touch Bar content](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-touchBar@2x.png)

## Parameters

- `content`: A collection of views to be displayed by the Touch Bar.

## See Also

### Managing Touch Bar input
- [func touchBar<Content>(TouchBar<Content>) -> some View](./touchbar%28_%29.md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/touchbar(content:))*