# defaultWidth(forInkType:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Type Method

Returns the default line width for the specified tool type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func defaultWidth(forInkType inkType: __PKInkType) -> CGFloat
```

```objc
+ (CGFloat) defaultWidthForInkType:(PKInkType) inkType;
```

## Return Value

The default line width (in points) for the specified tool type.

## Parameters

- `inkType`: The type of tool whose default line width you want.

## See Also

### Getting the standard ink widths
- [class func minimumWidth(forInkType: __PKInkType) -> CGFloat](./minimumwidth%28forinktype%29.md)
  Returns the minimum allowed line width for the specified tool type.
- [class func maximumWidth(forInkType: __PKInkType) -> CGFloat](./maximumwidth%28forinktype%29.md)
  Returns the maximum allowed line width for the specified tool type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/defaultwidth(forinktype:))*