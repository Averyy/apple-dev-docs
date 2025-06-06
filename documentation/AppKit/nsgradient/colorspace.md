# colorSpace

**Framework**: AppKit  
**Kind**: property

The color space of the colors associated with the gradient.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var colorSpace: NSColorSpace { get }
```

#### Discussion

When the receiver is initialized, colors that do not conform to the receiver’s color space are converted automatically.

## See Also

- [var numberOfColorStops: Int](nsgradient/numberofcolorstops.md)
  The number of color stops associated with the gradient.
- [func getColor(AutoreleasingUnsafeMutablePointer<NSColor>?, location: UnsafeMutablePointer<CGFloat>?, at: Int)](nsgradient/getcolor(_:location:at:).md)
  Returns information about the color stop at the specified index in the receiver’s color array.
- [func interpolatedColor(atLocation: CGFloat) -> NSColor](nsgradient/interpolatedcolor(atlocation:).md)
  Returns the color of the rendered gradient at the specified relative location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/colorspace)*