# TouchBar

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A container for a view that you can show in the Touch Bar.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct TouchBar<Content> where Content : View
```

## Topics

### Creating a Touch Bar view
- [init(content: () -> Content)](./touchbar/init%28content%29.md)
  Creates a non-customizable Touch Bar view container.
- [init(id: String, content: () -> Content)](./touchbar/init%28id,content%29.md)
  Creates a customizable Touch Bar view container with a globally unique identifier.

## See Also

### Managing Touch Bar input
- [func touchBar<Content>(content: () -> Content) -> some View](./view/touchbar%28content%29.md)
  Sets the content that the Touch Bar displays.
- [func touchBar<Content>(TouchBar<Content>) -> some View](./view/touchbar%28_%29.md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBarItemPrincipal(Bool) -> some View](./view/touchbaritemprincipal%28_%29.md)
  Sets principal views that have special significance to this Touch Bar.
- [func touchBarCustomizationLabel(Text) -> some View](./view/touchbarcustomizationlabel%28_%29.md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](./view/touchbaritempresence%28_%29.md)
  Sets the behavior of the user-customized view.
- [enum TouchBarItemPresence](./touchbaritempresence.md)
  Options that affect user customization of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/touchbar)*