# init(coder:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a gradient from data in an unarchiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Creating a Gradient
- [convenience init?(starting: NSColor, ending: NSColor)](./init%28starting,ending%29.md)
  Initializes a newly allocated gradient object with two colors.
- [convenience init?(colors: [NSColor])](./init%28colors%29.md)
  Initializes a newly allocated gradient object with an array of colors.
- [convenience init?(colorsAndLocations: (NSColor, CGFloat)...)](./init%28colorsandlocations%29.md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.
- [init?(colors: [NSColor], atLocations: UnsafePointer<CGFloat>?, colorSpace: NSColorSpace)](./init%28colors,atlocations,colorspace%29.md)
  Initializes a newly allocated gradient object with the specified colors, color locations, and color space.
- [- initWithColorsAndLocations:](./initwithcolorsandlocations_.md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/init(coder:))*