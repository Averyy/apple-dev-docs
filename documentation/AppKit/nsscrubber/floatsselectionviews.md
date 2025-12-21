# floatsSelectionViews

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines the behavior of the item selection decorations as the scrubber’s selection changes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var floatsSelectionViews: Bool { get set }
```

#### Discussion

When scrubber items are selected, they are decorated with background and overlay views, as determined by the [`selectionBackgroundStyle`](nsscrubber/selectionbackgroundstyle.md) and [`selectionOverlayStyle`](nsscrubber/selectionoverlaystyle.md) properties.

As the selection changes, the behavior of these selection decoration views is determined by the [`floatsSelectionViews`](nsscrubber/floatsselectionviews.md) property, as follows:

- [`true`](https://developer.apple.com/documentation/Swift/true) The overlay and background views float smoothly between the previously selected item and the newly selected item.
- [`false`](https://developer.apple.com/documentation/Swift/false) The overlay and background views cross-fade from the previously selected item to the newly selected item.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var selectionOverlayStyle: NSScrubberSelectionStyle?](nsscrubber/selectionoverlaystyle.md)
  The style overlaid on selected items.
- [var selectionBackgroundStyle: NSScrubberSelectionStyle?](nsscrubber/selectionbackgroundstyle.md)
  The style applied to the background of selected items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/floatsselectionviews)*