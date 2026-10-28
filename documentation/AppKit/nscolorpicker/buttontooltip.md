# buttonToolTip

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tool tip that is shown when the mouse cursor is over the color picker’s button image.

**Availability**:
- macOS

## Declaration

```swift
var buttonToolTip: String { get }
```

```objc
@property (copy, readonly) NSString * buttonToolTip;
```

## Discussion

Override this property’s getter method to provide a custom tool tip. The default implementation returns the name of the receiver’s class. If you want the color picker to have no tool tip, return an empty string.

## See Also

### Customizing the Color Picker
- [var minContentSize: NSSize](./mincontentsize.md)
  The minimum content size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpicker/buttontooltip)*