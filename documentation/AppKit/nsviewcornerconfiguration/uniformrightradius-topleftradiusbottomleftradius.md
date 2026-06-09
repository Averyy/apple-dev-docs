# uniformRightRadius(_:topLeftRadius:bottomLeftRadius:)

**Framework**: AppKit  
**Kind**: method

A configuration that applies the `rightRadius` uniformly to the top-right and bottom-right corners, with optional independent radii for the top-left and bottom-left corners. When the uniform corners differ, it uses the largest of the resolved corner radii.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class func uniformRightRadius(_ rightRadius: NSViewCornerRadius, topLeftRadius: NSViewCornerRadius?, bottomLeftRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration
```

## Parameters

- `rightRadius`: Radius for right edge.
- `topLeftRadius`: Radius for the top left corner.
- `bottomLeftRadius`: Radius for the bottom left corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration/uniformrightradius(_:topleftradius:bottomleftradius:))*