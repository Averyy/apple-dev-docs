# patternImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The pattern image used to paint the target area.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var patternImage: NSImage { get }
```

```objc
@property (copy, readonly) NSImage * patternImage;
```

#### Discussion

This property contains the image (instead of the solid color) to use during drawing. Pattern images are tiled as needed to fill the rendered area.

Do not access this property unless you created the color object using a pattern image. Accessing this property for colors created using other types of color information raises an exception.

## See Also

### Creating a pattern-based color
- [init(patternImage: NSImage)](./init%28patternimage%29.md)
  Creates a color object that uses the specified image pattern to paint the target area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/patternimage)*