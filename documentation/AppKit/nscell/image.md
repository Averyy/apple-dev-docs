# image

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image displayed by the cell, if any.

**Availability**:
- macOS

## Declaration

```swift
var image: NSImage? { get set }
```

```objc
@property (strong, nullable) NSImage * image;
```

#### Discussion

Setting the value of this property converts the cell to an image-type cell, if it is not one already. The value of this property is `nil` if the cell is not an image-type cell.

## See Also

### Related Documentation
- [var type: NSCell.CellType](./type.md)
  The type of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/image)*