# colorWithCGColor:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a color object using the specified Quartz color reference.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (UIColor *) colorWithCGColor:(CGColorRef) cgColor;
```

#### Return Value

The color object. The color information represented by this object is in the native colorspace of the specified Quartz color.

## Parameters

- `cgColor`: A reference to a Quartz color.

## See Also

### Creating a color from another color object
- [+ colorWithCIColor:](./colorwithcicolor_.md)
  Creates a color object that encapsulates a Core Image color.
- [init(ciColor: CIColor)](./init%28cicolor%29-2z057.md)
  Creates a color object that encapsulates a Core Image color.
- [init(cgColor: CGColor)](./init%28cgcolor%29-27r9g.md)
  Creates a color object using the specified Quartz color reference.
- [func withAlphaComponent(CGFloat) -> UIColor](./withalphacomponent%28_%29.md)
  Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/colorwithcgcolor:)*