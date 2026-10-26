# colorWithCIColor:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a color object that encapsulates a Core Image color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```objc
+ (UIColor *) colorWithCIColor:(CIColor *) ciColor;
```

#### Return Value

The `UIColor` object corresponding to the specified Core Image color.

## Parameters

- `ciColor`: The Core Image color to convert.

## See Also

### Creating a color from another color object
- [init(ciColor: CIColor)](./init%28cicolor%29-2z057.md)
  Creates a color object that encapsulates a Core Image color.
- [+ colorWithCGColor:](./colorwithcgcolor_.md)
  Creates a color object using the specified Quartz color reference.
- [init(cgColor: CGColor)](./init%28cgcolor%29-27r9g.md)
  Creates a color object using the specified Quartz color reference.
- [func withAlphaComponent(CGFloat) -> UIColor](./withalphacomponent%28_%29.md)
  Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/colorwithcicolor:)*