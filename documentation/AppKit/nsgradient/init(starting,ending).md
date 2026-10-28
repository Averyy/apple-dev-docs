# init(starting:ending:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated gradient object with two colors.

**Availability**:
- macOS 10.5+

## Declaration

```swift
convenience init?(starting startingColor: NSColor, ending endingColor: NSColor)
```

```objc
- (instancetype) initWithStartingColor:(NSColor *) startingColor endingColor:(NSColor *) endingColor;
```

## Return Value

The initialized `NSGradient` object.

## Parameters

- `startingColor`: The starting color of the gradient. The location of this color is fixed at 0.0.
- `endingColor`: The ending color of the gradient. The location of this color is fixed at 1.0.

## See Also

### Creating a Gradient
- [convenience init?(colors: [NSColor])](./init%28colors%29.md)
  Initializes a newly allocated gradient object with an array of colors.
- [convenience init?(colorsAndLocations: (NSColor, CGFloat)...)](./init%28colorsandlocations%29.md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.
- [init?(colors: [NSColor], atLocations: UnsafePointer<CGFloat>?, colorSpace: NSColorSpace)](./init%28colors,atlocations,colorspace%29.md)
  Initializes a newly allocated gradient object with the specified colors, color locations, and color space.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a gradient from data in an unarchiver.
- [- initWithColorsAndLocations:](./initwithcolorsandlocations_.md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/init(starting:ending:))*