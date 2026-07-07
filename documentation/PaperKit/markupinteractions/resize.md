# resize

**Framework**: PaperKit  
**Kind**: property

Allows resizing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let resize: MarkupInteractions
```

#### Discussion

This only controls manual resizing through direct interaction (drag handles, gestures). Programmatic resizing via the `frame` property always works. For `ShapeMarkup` elements, automatic content-driven resizing from the `autoresizing` property still occurs independently of this setting.

## See Also

- [static let rotate: MarkupInteractions](markupinteractions/rotate.md)
  Allows rotation.
- [static let move: MarkupInteractions](markupinteractions/move.md)
  Allows moving.
- [static let delete: MarkupInteractions](markupinteractions/delete.md)
  Allows deletion.
- [static let style: MarkupInteractions](markupinteractions/style.md)
  Allows style changes.
- [static let select: MarkupInteractions](markupinteractions/select.md)
  Allows selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupinteractions/resize)*