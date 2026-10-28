# init(colors:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated gradient object with an array of colors.

**Availability**:
- macOS 10.5+

## Declaration

```swift
convenience init?(colors colorArray: [NSColor])
```

```objc
- (instancetype) initWithColors:(NSArray<NSColor *> *) colorArray;
```

## Return Value

The initialized `NSGradient` object.

## Parameters

- `colorArray`: An array of `NSColor` objects representing the colors to use to initialize the gradient. There must be at least two colors in the array. The first color is placed at location 0.0 and the last at location 1.0. If there are more than two colors, the additional colors are placed at evenly spaced intervals between the first and last colors.

## See Also

### Creating a Gradient
- [convenience init?(starting: NSColor, ending: NSColor)](./init%28starting,ending%29.md)
  Initializes a newly allocated gradient object with two colors.
- [convenience init?(colorsAndLocations: (NSColor, CGFloat)...)](./init%28colorsandlocations%29.md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.
- [init?(colors: [NSColor], atLocations: UnsafePointer<CGFloat>?, colorSpace: NSColorSpace)](./init%28colors,atlocations,colorspace%29.md)
  Initializes a newly allocated gradient object with the specified colors, color locations, and color space.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a gradient from data in an unarchiver.
- [- initWithColorsAndLocations:](./initwithcolorsandlocations_.md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/init(colors:))*