# selectionOverlayStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The style overlaid on selected items.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var selectionOverlayStyle: NSScrubberSelectionStyle? { get set }
```

```objc
@property (strong, nullable) NSScrubberSelectionStyle * selectionOverlayStyle;
```

#### Discussion

The default value is `nil`, which specifies no overlay decoration.

You can either choose from one of the built-in selection styles ([`outlineOverlay`](../nsscrubberselectionstyle/outlineoverlay.md) or [`roundedBackground`](../nsscrubberselectionstyle/roundedbackground.md)), or you can subclass [`NSScrubberSelectionStyle`](../nsscrubberselectionstyle.md) to create your own custom selection style.

## See Also

### Configuring the selection appearance
- [var floatsSelectionViews: Bool](./floatsselectionviews.md)
  A Boolean value that determines the behavior of the item selection decorations as the scrubber’s selection changes.
- [var selectionBackgroundStyle: NSScrubberSelectionStyle?](./selectionbackgroundstyle.md)
  The style applied to the background of selected items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/selectionoverlaystyle)*