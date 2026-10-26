# initWithColorsAndLocations:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initializes a newly allocated gradient object with a comma-separated list of arguments.

**Availability**:
- macOS 10.5+

## Declaration

```objc
- (instancetype) initWithColorsAndLocations:(NSColor *) firstColor;
```

#### Return Value

The initialized `NSGradient` object.

#### Discussion

Optionally pass a comma-separated list of alternating `NSColor` objects and location arguments (specified as `CGFloat` values). The first value after `firstColor` must be a location. Each location value must be between 0.0 and 1.0. The list must be `nil`-terminated.

Typically, at least one color should have a location of 0.0 and one should have a location of 1.0. If these locations are not specified, the color at the closest color stop is used to fill the gap.

## Parameters

- `firstColor`: The first color in the gradient.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/initwithcolorsandlocations:)*