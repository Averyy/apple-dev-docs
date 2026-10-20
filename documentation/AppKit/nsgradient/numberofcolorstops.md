# numberOfColorStops

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of color stops associated with the gradient.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var numberOfColorStops: Int { get }
```

```objc
@property (readonly) NSInteger numberOfColorStops;
```

#### Discussion

Gradients must have at least two color stops: one defining the location of the start color and one defining the location of the end color. Gradients may have additional color stops located at different transition points in between the start and end stops.

## See Also

### Getting Gradient Properties
- [var colorSpace: NSColorSpace](./colorspace.md)
  The color space of the colors associated with the gradient.
- [func getColor(AutoreleasingUnsafeMutablePointer<NSColor>?, location: UnsafeMutablePointer<CGFloat>?, at: Int)](./getcolor%28_,location,at%29.md)
  Returns information about the color stop at the specified index in the receiver’s color array.
- [func interpolatedColor(atLocation: CGFloat) -> NSColor](./interpolatedcolor%28atlocation%29.md)
  Returns the color of the rendered gradient at the specified relative location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/numberofcolorstops)*