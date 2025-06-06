# MenuButton

**Framework**: SwiftUI  
**Kind**: struct

A button that displays a menu containing a list of choices when pressed.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct MenuButton<Label, Content> where Label : View, Content : View
```

## Topics

### Creating a menu button
- [init(_:content:)](menubutton/init(_:content:).md)
  Creates a menu button with the specified localized title and content.
- [init(label: Label, content: () -> Content)](menubutton/init(label:content:).md)
  Creates a menu button with the specified label and content.
### Styling a menu button
- [func menuButtonStyle<S>(S) -> some View](view/menubuttonstyle(_:).md)
  Sets the style for menu buttons within this view.
- [protocol MenuButtonStyle](menubuttonstyle.md)
  A custom specification for the appearance and interaction of a menu button.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [typealias PullDownButton](pulldownbutton.md)
- [struct ContextMenu](contextmenu.md)
  A container for views that you present as menu items in a context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubutton)*