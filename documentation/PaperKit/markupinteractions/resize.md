# resize

**Framework**: PaperKit  
**Kind**: property  
**Role**: Type Property

Allows resizing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static let resize: MarkupInteractions
```

## Discussion

This only controls manual resizing through direct interaction (drag handles, gestures). Programmatic resizing via the `frame` property always works. For `ShapeMarkup` elements, automatic content-driven resizing from the `autoresizing` property still occurs independently of this setting.

## See Also

### Configuring interactions
- [static let rotate: MarkupInteractions](./rotate.md)
  Allows rotation.
- [static let move: MarkupInteractions](./move.md)
  Allows moving.
- [static let delete: MarkupInteractions](./delete.md)
  Allows deletion.
- [static let style: MarkupInteractions](./style.md)
  Allows style changes.
- [static let select: MarkupInteractions](./select.md)
  Allows selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupinteractions/resize)*