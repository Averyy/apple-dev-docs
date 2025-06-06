# TouchBar

**Framework**: SwiftUI  
**Kind**: struct

A container for a view that you can show in the Touch Bar.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct TouchBar<Content> where Content : View
```

## Topics

### Creating a Touch Bar view
- [init(content: () -> Content)](touchbar/init(content:).md)
  Creates a non-customizable Touch Bar view container.
- [init(id: String, content: () -> Content)](touchbar/init(id:content:).md)
  Creates a customizable Touch Bar view container with a globally unique identifier.

## See Also

- [func touchBar<Content>(content: () -> Content) -> some View](view/touchbar(content:).md)
  Sets the content that the Touch Bar displays.
- [func touchBar<Content>(TouchBar<Content>) -> some View](view/touchbar(_:).md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBarItemPrincipal(Bool) -> some View](view/touchbaritemprincipal(_:).md)
  Sets principal views that have special significance to this Touch Bar.
- [func touchBarCustomizationLabel(Text) -> some View](view/touchbarcustomizationlabel(_:).md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](view/touchbaritempresence(_:).md)
  Sets the behavior of the user-customized view.
- [enum TouchBarItemPresence](touchbaritempresence.md)
  Options that affect user customization of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/touchbar)*