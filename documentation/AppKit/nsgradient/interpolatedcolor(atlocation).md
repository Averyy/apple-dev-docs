# interpolatedColor(atLocation:)

**Framework**: AppKit  
**Kind**: method

Returns the color of the rendered gradient at the specified relative location.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func interpolatedColor(atLocation location: CGFloat) -> NSColor
```

#### Discussion

This method does not simply return the color values used to initialize the receiver. Instead, it computes the value that would be drawn at the specified location.

The start color of the gradient is always located at 0.0 and the end color is always at 1.0.

## Parameters

- `location`: The location value for the color you want. This value must be between 0.0 and 1.0. This value need not correspond to the location of one of the color objects used to create the gradient.

## See Also

- [var colorSpace: NSColorSpace](nsgradient/colorspace.md)
  The color space of the colors associated with the gradient.
- [var numberOfColorStops: Int](nsgradient/numberofcolorstops.md)
  The number of color stops associated with the gradient.
- [func getColor(AutoreleasingUnsafeMutablePointer<NSColor>?, location: UnsafeMutablePointer<CGFloat>?, at: Int)](nsgradient/getcolor(_:location:at:).md)
  Returns information about the color stop at the specified index in the receiver’s color array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/interpolatedcolor(atlocation:))*