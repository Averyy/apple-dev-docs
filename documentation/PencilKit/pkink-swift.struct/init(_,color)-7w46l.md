# init(_:color:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates a new ink, specifying its type and color.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(_ inkType: PKInk.InkType, color: NSColor = NSColor.black)
```

## Parameters

- `inkType`: The type of ink represented by one of the available [`PKInkingTool.InkType`](../pkinkingtool-swift.struct/inktype-swift.enum.md) enumerations.
- `color`: The color of the ink, defaults to black.

## See Also

### Creating an ink object
- [init(PKInk.InkType, color: UIColor)](./init%28_,color%29-2rx09.md)
  Creates a new ink, specifying its type and color.
- [typealias InkType](./inktype-swift.typealias.md)
  A type alias referring to the ink type of an inking tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkink-swift.struct/init(_:color:)-7w46l)*