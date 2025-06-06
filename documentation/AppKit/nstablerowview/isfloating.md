# isFloating

**Framework**: AppKit  
**Kind**: property

Specifies whether the row is drawn using the floating style.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var isFloating: Bool { get set }
```

#### Discussion

Floating is a temporary attribute that is set when a particular group row is actually floating above other rows. The state may change dynamically based on the position of the group row. Drawing may be different for rows that are currently ‘floating’.

## See Also

- [var isEmphasized: Bool](nstablerowview/isemphasized.md)
  Determines whether the row will draw with the alternate or secondary color (unless overridden).
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nstablerowview/interiorbackgroundstyle.md)
  Specifies how the subviews should draw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/isfloating)*