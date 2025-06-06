# init(colorsAndLocations:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated gradient object with a comma-separated list of arguments.

**Availability**:
- macOS 10.9+

## Declaration

```swift
convenience init?(colorsAndLocations objects: (NSColor, CGFloat)...)
```

## See Also

- [convenience init?(starting: NSColor, ending: NSColor)](nsgradient/init(starting:ending:).md)
  Initializes a newly allocated gradient object with two colors.
- [convenience init?(colors: [NSColor])](nsgradient/init(colors:).md)
  Initializes a newly allocated gradient object with an array of colors.
- [init?(colors: [NSColor], atLocations: UnsafePointer<CGFloat>?, colorSpace: NSColorSpace)](nsgradient/init(colors:atlocations:colorspace:).md)
  Initializes a newly allocated gradient object with the specified colors, color locations, and color space.
- [init?(coder: NSCoder)](nsgradient/init(coder:).md)
  Creates a gradient from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/init(colorsandlocations:))*