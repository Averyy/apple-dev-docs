# init(colors:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated gradient object with an array of colors.

**Availability**:
- macOS 10.5+

## Declaration

```swift
convenience init?(colors colorArray: [NSColor])
```

#### Return Value

The initialized `NSGradient` object.

## Parameters

- `colorArray`: An array of   objects representing the colors to use to initialize the gradient. There must be at least two colors in the array. The first color is placed at location 0.0 and the last at location 1.0. If there are more than two colors, the additional colors are placed at evenly spaced intervals between the first and last colors.

## See Also

- [convenience init?(starting: NSColor, ending: NSColor)](nsgradient/init(starting:ending:).md)
  Initializes a newly allocated gradient object with two colors.
- [convenience init?(colorsAndLocations: (NSColor, CGFloat)...)](nsgradient/init(colorsandlocations:).md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.
- [init?(colors: [NSColor], atLocations: UnsafePointer<CGFloat>?, colorSpace: NSColorSpace)](nsgradient/init(colors:atlocations:colorspace:).md)
  Initializes a newly allocated gradient object with the specified colors, color locations, and color space.
- [init?(coder: NSCoder)](nsgradient/init(coder:).md)
  Creates a gradient from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/init(colors:))*