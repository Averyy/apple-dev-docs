# selectionOverlayStyle

**Framework**: AppKit  
**Kind**: property

The style overlaid on selected items.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var selectionOverlayStyle: NSScrubberSelectionStyle? { get set }
```

#### Discussion

The default value is `nil`, which specifies no overlay decoration.

You can either choose from one of the built-in selection styles ([`outlineOverlay`](nsscrubberselectionstyle/outlineoverlay.md) or [`roundedBackground`](nsscrubberselectionstyle/roundedbackground.md)), or you can subclass [`NSScrubberSelectionStyle`](nsscrubberselectionstyle.md) to create your own custom selection style.

## See Also

- [var floatsSelectionViews: Bool](nsscrubber/floatsselectionviews.md)
  A Boolean value that determines the behavior of the item selection decorations as the scrubber’s selection changes.
- [var selectionBackgroundStyle: NSScrubberSelectionStyle?](nsscrubber/selectionbackgroundstyle.md)
  The style applied to the background of selected items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/selectionoverlaystyle)*