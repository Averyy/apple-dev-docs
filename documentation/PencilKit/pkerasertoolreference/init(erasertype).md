# init(eraserType:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates an eraser tool object that removes objects wholly or partially from a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(eraserType: __PKEraserType)
```

```objc
- (instancetype) initWithEraserType:(PKEraserType) eraserType;
```

#### Return Value

A new eraser tool object.

## Parameters

- `eraserType`: A constant that determines how the eraser affects drawn content. For a list of possible values, see [`PKEraserType`](../pkerasertype.md).

## See Also

### Creating an eraser tool
- [init(eraserType: __PKEraserType, width: CGFloat)](./init%28erasertype,width%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkerasertoolreference/init(erasertype:))*