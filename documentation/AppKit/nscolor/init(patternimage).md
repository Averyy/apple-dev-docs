# init(patternImage:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object that uses the specified image pattern to paint the target area.

**Availability**:
- macOS

## Declaration

```swift
init(patternImage image: NSImage)
```

```objc
+ (NSColor *) colorWithPatternImage:(NSImage *) image;
```

#### Return Value

The `NSColor` object. This color object is autoreleased.

## Parameters

- `image`: The image to use as the pattern for the color object. The image is tiled starting at the bottom of the window. The image is not scaled.

## See Also

### Creating a pattern-based color
- [var patternImage: NSImage](./patternimage.md)
  The pattern image used to paint the target area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(patternimage:))*