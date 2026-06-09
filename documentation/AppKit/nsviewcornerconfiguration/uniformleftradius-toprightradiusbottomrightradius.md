# uniformLeftRadius(_:topRightRadius:bottomRightRadius:)

**Framework**: AppKit  
**Kind**: method

A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, with optional independent radii for the top-right and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class func uniformLeftRadius(_ leftRadius: NSViewCornerRadius, topRightRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration
```

## Parameters

- `leftRadius`: Radius for left edge.
- `topRightRadius`: Radius for the top right corner.
- `bottomRightRadius`: Radius for the bottom right corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration/uniformleftradius(_:toprightradius:bottomrightradius:))*