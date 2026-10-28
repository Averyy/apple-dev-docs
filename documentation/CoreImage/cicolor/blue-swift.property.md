# blue

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

Returns the unpremultiplied blue component of the color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var blue: CGFloat { get }
```

```objc
@property (readonly) CGFloat blue;
```

## Discussion

If the [`CIColor`](../cicolor.md) was initialized with a `CGColor` in a non-RGB `CGColorSpace` then it will be converted to sRGB to get the green component.

## See Also

### Getting Color Components
- [var colorSpace: CGColorSpace](./colorspace.md)
  Returns the `CGColorSpace` associated with the color
- [var components: UnsafePointer<CGFloat>](./components.md)
  Return a pointer to an array of `CGFloat` values including alpha.
- [var numberOfComponents: Int](./numberofcomponents.md)
  Returns the color components of the color including alpha.
- [var red: CGFloat](./red-swift.property.md)
  Returns the unpremultiplied red component of the color.
- [var green: CGFloat](./green-swift.property.md)
  Returns the unpremultiplied green component of the color.
- [var alpha: CGFloat](./alpha.md)
  Returns the alpha value of the color.
- [var stringRepresentation: String](./stringrepresentation.md)
  Returns a formatted string with the unpremultiplied color and alpha components of the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/blue-swift.property)*