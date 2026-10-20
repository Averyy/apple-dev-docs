# init(colorsAndLocations:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated gradient object with a comma-separated list of arguments.

**Availability**:
- macOS 10.9+

## Declaration

```swift
convenience init?(colorsAndLocations objects: (NSColor, CGFloat)...)
```

## See Also

### Creating a Gradient
- [convenience init?(starting: NSColor, ending: NSColor)](./init%28starting,ending%29.md)
  Initializes a newly allocated gradient object with two colors.
- [convenience init?(colors: [NSColor])](./init%28colors%29.md)
  Initializes a newly allocated gradient object with an array of colors.
- [init?(colors: [NSColor], atLocations: UnsafePointer<CGFloat>?, colorSpace: NSColorSpace)](./init%28colors,atlocations,colorspace%29.md)
  Initializes a newly allocated gradient object with the specified colors, color locations, and color space.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a gradient from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/init(colorsandlocations:))*