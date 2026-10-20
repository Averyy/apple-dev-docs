# isBordered

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the text field draws a solid black border around its contents.

**Availability**:
- macOS

## Declaration

```swift
var isBordered: Bool { get set }
```

```objc
@property (getter=isBordered) BOOL bordered;
```

#### Discussion

If [`true`](../../Swift/true.md), the text field draws a border; if [`false`](../../Swift/false.md), it doesn’t draw a border.

## See Also

### Setting a border
- [var borderShape: NSControl.BorderShape](./bordershape.md)
  Set border shape `NSControlBorderShapeAutomatic` sets text field or subclass to default system shape. `NSControlBorderShapeCircle` sets text field or subclass to `NSControlBorderShapeAutomatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/isbordered)*