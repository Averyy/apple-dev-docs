# changeBackgroundCellMask

**Framework**: AppKit  
**Kind**: property

Same as `NSChangeGrayCellMask`, but only background pixels are changed.

**Availability**:
- macOS ?+

## Declaration

```swift
static var changeBackgroundCellMask: NSCell.StyleMask { get }
```

## See Also

- [static var pushInCellMask: NSCell.StyleMask](nscell/stylemask/pushincellmask.md)
  The button cell “pushes in” if it has a border.
- [static var contentsCellMask: NSCell.StyleMask](nscell/stylemask/contentscellmask.md)
  The button cell displays its alternate icon and/or title.
- [static var changeGrayCellMask: NSCell.StyleMask](nscell/stylemask/changegraycellmask.md)
  The button cell swaps the “control color” (the [`controlColor`](nscolor/controlcolor.md) method of `NSColor`) and white pixels on its background and icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/stylemask/changebackgroundcellmask)*