# components

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

Return a pointer to an array of `CGFloat` values including alpha.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var components: UnsafePointer<CGFloat> { get }
```

```objc
@property (readonly) const CGFloat * components;
```

## Discussion

Typically this array will contain `4` `CGFloat` values for red, green, blue, and alpha. If the [`CIColor`](../cicolor.md) was initialized with a `CGColor` then returned pointer will be the same as calling `CGColorGetComponents()`

## See Also

### Getting Color Components
- [var colorSpace: CGColorSpace](./colorspace.md)
  Returns the `CGColorSpace` associated with the color
- [var numberOfComponents: Int](./numberofcomponents.md)
  Returns the color components of the color including alpha.
- [var red: CGFloat](./red-swift.property.md)
  Returns the unpremultiplied red component of the color.
- [var green: CGFloat](./green-swift.property.md)
  Returns the unpremultiplied green component of the color.
- [var blue: CGFloat](./blue-swift.property.md)
  Returns the unpremultiplied blue component of the color.
- [var alpha: CGFloat](./alpha.md)
  Returns the alpha value of the color.
- [var stringRepresentation: String](./stringrepresentation.md)
  Returns a formatted string with the unpremultiplied color and alpha components of the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/components)*