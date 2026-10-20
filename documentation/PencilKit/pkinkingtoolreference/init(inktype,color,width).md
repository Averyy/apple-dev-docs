# init(inkType:color:width:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates an ink tool object with the specified color and line width values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
init(inkType type: __PKInkType, color: UIColor, width: CGFloat)
```

*macOS*

```swift
init(inkType type: __PKInkType, color: NSColor, width: CGFloat)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (instancetype) initWithInkType:(PKInkType) type color:(UIColor *) color width:(CGFloat) width;
```

*macOS*

```objc
- (instancetype) initWithInkType:(PKInkType) type color:(NSColor *) color width:(CGFloat) width;
```

#### Return Value

A new inking tool with the specified type, color, and width.

## Parameters

- `type`: The shape of the tool. You may specify [`PKInkTypeMarker`](../pkinktypemarker.md), [`PKInkTypePen`](../pkinktypepen.md), or [`PKInkTypePencil`](../pkinktypepencil.md).
- `color`: The color to apply to drawn lines.
- `width`: The base width to apply to any drawn lines. The value in the `inkType` parameter and input from Apple Pencil affects the final actual width.

## See Also

### Creating an inking tool
- [convenience init(inkType: __PKInkType, color: UIColor)](./init%28inktype,color%29.md)
  Creates an ink tool object with the default line width and the specified color.
- [convenience init(ink: PKInk, width: CGFloat)](./init%28ink,width%29.md)
  Create an inking tool with the specified ink and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/init(inktype:color:width:))*