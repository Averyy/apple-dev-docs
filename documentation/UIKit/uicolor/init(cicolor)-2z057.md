# init(ciColor:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a color object that encapsulates a Core Image color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(ciColor: CIColor)
```

```objc
- (UIColor *) initWithCIColor:(CIColor *) ciColor;
```

## Return Value

An initialized color object.

## Parameters

- `ciColor`: The Core Image color to convert.

## See Also

### Creating a color from another color object
- [convenience init(Color)](./init%28_%29.md)
  Creates a color object that encapsulates a SwiftUI color.
- [init(cgColor: CGColor)](./init%28cgcolor%29-27r9g.md)
  Creates a color object using the specified Quartz color reference.
- [func withAlphaComponent(CGFloat) -> UIColor](./withalphacomponent%28_%29.md)
  Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.
- [+ colorWithCIColor:](./colorwithcicolor_.md)
  Creates a color object that encapsulates a Core Image color.
- [+ colorWithCGColor:](./colorwithcgcolor_.md)
  Creates a color object using the specified Quartz color reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(cicolor:)-2z057)*