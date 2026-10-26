# contentsCellMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The button cell displays its alternate icon and/or title.

**Availability**:
- macOS

## Declaration

```swift
static var contentsCellMask: NSCell.StyleMask { get }
```

```c
NSContentsCellMask
```

## See Also

### Constants
- [static var pushInCellMask: NSCell.StyleMask](./pushincellmask.md)
  The button cell “pushes in” if it has a border.
- [static var changeGrayCellMask: NSCell.StyleMask](./changegraycellmask.md)
  The button cell swaps the “control color” (the [`controlColor`](../../nscolor/controlcolor.md) method of `NSColor`) and white pixels on its background and icon.
- [static var changeBackgroundCellMask: NSCell.StyleMask](./changebackgroundcellmask.md)
  Same as `NSChangeGrayCellMask`, but only background pixels are changed.
- [NSNoCellMask](../../nscellstylemask/nsnocellmask.md)
  The button cell doesn’t change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/stylemask/contentscellmask)*