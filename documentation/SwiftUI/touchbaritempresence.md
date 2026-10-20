# TouchBarItemPresence

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

Options that affect user customization of the Touch Bar.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum TouchBarItemPresence
```

## Topics

### Getting presence options
- [TouchBarItemPresence.default(_:)](./touchbaritempresence/default%28_%29.md)
  The Touch Bar view is visible by default, but can be removed during customization.
- [TouchBarItemPresence.optional(_:)](./touchbaritempresence/optional%28_%29.md)
  The Touch Bar view isn’t visible by default, but appears in the customization palette.
- [TouchBarItemPresence.required(_:)](./touchbaritempresence/required%28_%29.md)
  The Touch Bar view is visible by default and cannot be removed during customization.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [struct TouchBar](./touchbar.md)
  A container for a view that you can show in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/touchbaritempresence)*