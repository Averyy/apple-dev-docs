# init(starting:ending:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated gradient object with two colors.

**Availability**:
- macOS 10.5+

## Declaration

```swift
convenience init?(starting startingColor: NSColor, ending endingColor: NSColor)
```

#### Return Value

The initialized `NSGradient` object.

## Parameters

- `startingColor`: The starting color of the gradient. The location of this color is fixed at 0.0.
- `endingColor`: The ending color of the gradient. The location of this color is fixed at 1.0.

## See Also

- [Cocoa Drawing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)
- [convenience init?(colors: [NSColor])](nsgradient/init(colors:).md)
  Initializes a newly allocated gradient object with an array of colors.
- [convenience init?(colorsAndLocations: (NSColor, CGFloat)...)](nsgradient/init(colorsandlocations:).md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.
- [init?(colors: [NSColor], atLocations: UnsafePointer<CGFloat>?, colorSpace: NSColorSpace)](nsgradient/init(colors:atlocations:colorspace:).md)
  Initializes a newly allocated gradient object with the specified colors, color locations, and color space.
- [init?(coder: NSCoder)](nsgradient/init(coder:).md)
  Creates a gradient from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/init(starting:ending:))*