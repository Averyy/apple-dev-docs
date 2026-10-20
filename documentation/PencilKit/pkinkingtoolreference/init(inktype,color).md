# init(inkType:color:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates an ink tool object with the default line width and the specified color.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
convenience init(inkType type: __PKInkType, color: UIColor)
```

*macOS*

```swift
convenience init(inkType type: __PKInkType, color: NSColor)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (instancetype) initWithInkType:(PKInkType) type color:(UIColor *) color;
```

*macOS*

```objc
- (instancetype) initWithInkType:(PKInkType) type color:(NSColor *) color;
```

#### Return Value

A new inking tool with the specified type and color.

#### Discussion

This method sets the line width to the value returned by [`defaultWidth(forInkType:)`](./defaultwidth%28forinktype%29.md).

## Parameters

- `type`: The shape of the tool. You may specify [`PKInkTypeMarker`](../pkinktypemarker.md), [`PKInkTypePen`](../pkinktypepen.md), or [`PKInkTypePencil`](../pkinktypepencil.md).
- `color`: The color to apply to drawn lines.

## See Also

### Creating an inking tool
- [init(inkType: __PKInkType, color: UIColor, width: CGFloat)](./init%28inktype,color,width%29.md)
  Creates an ink tool object with the specified color and line width values.
- [convenience init(ink: PKInk, width: CGFloat)](./init%28ink,width%29.md)
  Create an inking tool with the specified ink and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/init(inktype:color:))*