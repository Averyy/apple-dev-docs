# accessibilityOrderedByRow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the accessibility element’s grid is in row major order or in column major order.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (getter=isAccessibilityOrderedByRow) BOOL accessibilityOrderedByRow;
```

#### Discussion

Use this property for UI elements that present a grid of child elements. Set the property to [`true`](../../Swift/true.md) if the grid is ordered row major; otherwise, set to [`false`](../../Swift/false.md).

## See Also

### Configuring grid views
- [accessibilityColumnCount](./accessibilitycolumncount.md)
  The number of columns in the accessibility element’s grid.
- [accessibilityRowCount](./accessibilityrowcount.md)
  The number of rows in the accessibility element’s grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityorderedbyrow)*