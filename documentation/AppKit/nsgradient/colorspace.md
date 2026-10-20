# colorSpace

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color space of the colors associated with the gradient.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var colorSpace: NSColorSpace { get }
```

```objc
@property (strong, readonly) NSColorSpace * colorSpace;
```

#### Discussion

When the receiver is initialized, colors that do not conform to the receiver’s color space are converted automatically.

## See Also

### Getting Gradient Properties
- [var numberOfColorStops: Int](./numberofcolorstops.md)
  The number of color stops associated with the gradient.
- [func getColor(AutoreleasingUnsafeMutablePointer<NSColor>?, location: UnsafeMutablePointer<CGFloat>?, at: Int)](./getcolor%28_,location,at%29.md)
  Returns information about the color stop at the specified index in the receiver’s color array.
- [func interpolatedColor(atLocation: CGFloat) -> NSColor](./interpolatedcolor%28atlocation%29.md)
  Returns the color of the rendered gradient at the specified relative location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/colorspace)*