# init(cgColor:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a color object using the specified Quartz color reference.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(cgColor: CGColor)
```

```objc
- (UIColor *) initWithCGColor:(CGColorRef) cgColor;
```

#### Return Value

An initialized color object. The color information represented by this object is in the native colorspace of the specified Quartz color.

## Parameters

- `cgColor`: A reference to a Quartz color.

## See Also

### Creating a color from another color object
- [convenience init(Color)](./init%28_%29.md)
  Creates a color object that encapsulates a SwiftUI color.
- [init(ciColor: CIColor)](./init%28cicolor%29-2z057.md)
  Creates a color object that encapsulates a Core Image color.
- [func withAlphaComponent(CGFloat) -> UIColor](./withalphacomponent%28_%29.md)
  Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.
- [+ colorWithCIColor:](./colorwithcicolor_.md)
  Creates a color object that encapsulates a Core Image color.
### Related Documentation
- [+ colorWithCGColor:](./colorwithcgcolor_.md)
  Creates a color object using the specified Quartz color reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(cgcolor:)-27r9g)*