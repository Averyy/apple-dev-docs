# cell

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s cell object.

**Availability**:
- macOS

## Declaration

```swift
var cell: NSCell? { get set }
```

```objc
@property (strong, nullable) NSCell * cell;
```

## Discussion

For controls with multiple cells (such as `NSMatrix` or `NSForm`), use the [`selectedCell()`](./selectedcell%28%29.md) property to retrieve a specific cell.

## See Also

### Deprecated properties
- [class var cellClass: AnyClass?](./cellclass.md)
  Returns the type of cell used by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/cell)*