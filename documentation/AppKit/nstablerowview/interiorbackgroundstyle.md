# interiorBackgroundStyle

**Framework**: AppKit  
**Kind**: property

Specifies how the subviews should draw.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var interiorBackgroundStyle: NSView.BackgroundStyle { get }
```

#### Discussion

This value is dynamically computed based on the set of properties set for the `NSTableRowView`.

Subclassers can override this value when they draw differently based on the currently displayed properties.

This property can also be set to determine the color a subview should use. See [`NSView.BackgroundStyle`](nsview/backgroundstyle.md) for supported values.

## See Also

- [var isEmphasized: Bool](nstablerowview/isemphasized.md)
  Determines whether the row will draw with the alternate or secondary color (unless overridden).
- [var isFloating: Bool](nstablerowview/isfloating.md)
  Specifies whether the row is drawn using the floating style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/interiorbackgroundstyle)*