# uniformTopRadius(_:bottomLeftRadius:bottomRightRadius:)

**Framework**: AppKit  
**Kind**: method

A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, with optional independent radii for the bottom-left and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class func uniformTopRadius(_ topRadius: NSViewCornerRadius, bottomLeftRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration
```

## Parameters

- `topRadius`: Radius for top edge.
- `bottomLeftRadius`: Radius for the bottom left corner.
- `bottomRightRadius`: Radius for the bottom right corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration/uniformtopradius(_:bottomleftradius:bottomrightradius:))*