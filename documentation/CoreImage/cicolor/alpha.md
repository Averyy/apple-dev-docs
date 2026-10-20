# alpha

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

Returns the alpha value of the color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var alpha: CGFloat { get }
```

```objc
@property (readonly) CGFloat alpha;
```

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
- [var blue: CGFloat](./blue-swift.property.md)
  Returns the unpremultiplied blue component of the color.
- [var stringRepresentation: String](./stringrepresentation.md)
  Returns a formatted string with the unpremultiplied color and alpha components of the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/alpha)*