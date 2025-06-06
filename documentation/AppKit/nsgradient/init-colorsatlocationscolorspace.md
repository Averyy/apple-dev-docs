# init(colors:atLocations:colorSpace:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated gradient object with the specified colors, color locations, and color space.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(colors colorArray: [NSColor], atLocations locations: UnsafePointer<CGFloat>?, colorSpace: NSColorSpace)
```

#### Return Value

The initialized `NSGradient` object.

#### Discussion

This method is the designated initializer of `NSGradient`. The colors in the `colorArray` parameter are converted to the specified color space if they are not already in that color space.

Typically, at least one color should have a location of 0.0 and one should have a location of 1.0. If these locations are not specified, the color at the closest color stop is used to fill the gap.

## Parameters

- `colorArray`: An array of   objects representing the colors in the gradient.
- `locations`: An array of   values containing the location for each color in the gradient. Each value must be in the range 0.0 to 1.0. There must be the same number of locations as are colors in the   parameter.
- `colorSpace`: The color space to use for the gradient.

## See Also

- [convenience init?(starting: NSColor, ending: NSColor)](nsgradient/init(starting:ending:).md)
  Initializes a newly allocated gradient object with two colors.
- [convenience init?(colors: [NSColor])](nsgradient/init(colors:).md)
  Initializes a newly allocated gradient object with an array of colors.
- [convenience init?(colorsAndLocations: (NSColor, CGFloat)...)](nsgradient/init(colorsandlocations:).md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.
- [init?(coder: NSCoder)](nsgradient/init(coder:).md)
  Creates a gradient from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/init(colors:atlocations:colorspace:))*