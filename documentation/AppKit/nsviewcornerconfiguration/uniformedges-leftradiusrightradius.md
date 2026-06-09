# uniformEdges(leftRadius:rightRadius:)

**Framework**: AppKit  
**Kind**: method

A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, and the `rightRadius` uniformly to the top-right and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class func uniformEdges(leftRadius: NSViewCornerRadius, rightRadius: NSViewCornerRadius) -> NSViewCornerConfiguration
```

## Parameters

- `leftRadius`: Radius for left edge.
- `rightRadius`: Radius for the right edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration/uniformedges(leftradius:rightradius:))*