# uniformBottomRadius(_:topLeftRadius:topRightRadius:)

**Framework**: AppKit  
**Kind**: method

A configuration that applies the `bottomRadius` uniformly to the bottom-left and bottom-right corners, with optional independent radii for the top-left and top-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class func uniformBottomRadius(_ bottomRadius: NSViewCornerRadius, topLeftRadius: NSViewCornerRadius?, topRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration
```

## Parameters

- `bottomRadius`: Radius for bottom edge.
- `topLeftRadius`: Radius for the top left corner.
- `topRightRadius`: Radius for the top right corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration/uniformbottomradius(_:topleftradius:toprightradius:))*