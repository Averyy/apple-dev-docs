# init(_:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates an eraser tool object that removes objects wholly or partially from a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(_ eraserType: PKEraserTool.EraserType)
```

#### Discussion

This initializer creates a new eraser tool object.

## Parameters

- `eraserType`: A constant that determines how the eraser affects drawn content. For a list of possible values, see [`PKEraserTool.EraserType`](./erasertype-swift.enum.md).

## See Also

### Creating an eraser tool
- [init(PKEraserTool.EraserType, width: CGFloat)](./init%28_,width%29.md)
  Creates an eraser tool object with the specified width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkerasertool-swift.struct/init(_:))*