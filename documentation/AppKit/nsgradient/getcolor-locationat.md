# getColor(_:location:at:)

**Framework**: AppKit  
**Kind**: method

Returns information about the color stop at the specified index in the receiver’s color array.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func getColor(_ color: AutoreleasingUnsafeMutablePointer<NSColor>?, location: UnsafeMutablePointer<CGFloat>?, at index: Int)
```

#### Discussion

This method returns the color stop information that was used to create the receiver. It does not return the interpolated color values at any point along the gradient. The location of the gradient’s first color is typically 0.0 and the location of the last color is typically 1.0, although the locations can vary depending on how the receiver was created.

## Parameters

- `color`: On input, a pointer to a color object. On output, the color at the specified index in the receiver’s color array. You may specify   if you are not interested in this parameter.
- `location`: On input, a pointer to a floating point number. On output, contains the location value associated with the color. This value is between 0.0 and 1.0. It is used to determine the position of the color relative to the start and end points of the gradient. You may specify   if you are not interested in this parameter.
- `index`: The index of the color you want.

## See Also

- [var colorSpace: NSColorSpace](nsgradient/colorspace.md)
  The color space of the colors associated with the gradient.
- [var numberOfColorStops: Int](nsgradient/numberofcolorstops.md)
  The number of color stops associated with the gradient.
- [func interpolatedColor(atLocation: CGFloat) -> NSColor](nsgradient/interpolatedcolor(atlocation:).md)
  Returns the color of the rendered gradient at the specified relative location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/getcolor(_:location:at:))*