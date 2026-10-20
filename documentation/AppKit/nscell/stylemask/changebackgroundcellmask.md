# changeBackgroundCellMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Same as `NSChangeGrayCellMask`, but only background pixels are changed.

**Availability**:
- macOS

## Declaration

```swift
static var changeBackgroundCellMask: NSCell.StyleMask { get }
```

```c
NSChangeBackgroundCellMask
```

## See Also

### Constants
- [static var pushInCellMask: NSCell.StyleMask](./pushincellmask.md)
  The button cell “pushes in” if it has a border.
- [static var contentsCellMask: NSCell.StyleMask](./contentscellmask.md)
  The button cell displays its alternate icon and/or title.
- [static var changeGrayCellMask: NSCell.StyleMask](./changegraycellmask.md)
  The button cell swaps the “control color” (the [`controlColor`](../../nscolor/controlcolor.md) method of `NSColor`) and white pixels on its background and icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/stylemask/changebackgroundcellmask)*