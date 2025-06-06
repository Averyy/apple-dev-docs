# TouchBarItemPresence

**Framework**: SwiftUI  
**Kind**: enum

Options that affect user customization of the Touch Bar.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum TouchBarItemPresence
```

## Topics

### Getting presence options
- [TouchBarItemPresence.default(_:)](touchbaritempresence/default(_:).md)
  The Touch Bar view is visible by default, but can be removed during customization.
- [TouchBarItemPresence.optional(_:)](touchbaritempresence/optional(_:).md)
  The Touch Bar view isn’t visible by default, but appears in the customization palette.
- [TouchBarItemPresence.required(_:)](touchbaritempresence/required(_:).md)
  The Touch Bar view is visible by default and cannot be removed during customization.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

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
- [struct TouchBar](touchbar.md)
  A container for a view that you can show in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/touchbaritempresence)*