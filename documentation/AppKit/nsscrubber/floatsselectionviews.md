# floatsSelectionViews

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines the behavior of the item selection decorations as the scrubber’s selection changes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var floatsSelectionViews: Bool { get set }
```

```objc
@property BOOL floatsSelectionViews;
```

## Discussion

When scrubber items are selected, they are decorated with background and overlay views, as determined by the [`selectionBackgroundStyle`](./selectionbackgroundstyle.md) and [`selectionOverlayStyle`](./selectionoverlaystyle.md) properties.

As the selection changes, the behavior of these selection decoration views is determined by the [`floatsSelectionViews`](./floatsselectionviews.md) property, as follows:

- [`true`](../../Swift/true.md) The overlay and background views float smoothly between the previously selected item and the newly selected item.
- [`false`](../../Swift/false.md) The overlay and background views cross-fade from the previously selected item to the newly selected item.

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring the selection appearance
- [var selectionOverlayStyle: NSScrubberSelectionStyle?](./selectionoverlaystyle.md)
  The style overlaid on selected items.
- [var selectionBackgroundStyle: NSScrubberSelectionStyle?](./selectionbackgroundstyle.md)
  The style applied to the background of selected items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/floatsselectionviews)*