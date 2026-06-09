# uniformEdges(topRadius:bottomRadius:)

**Framework**: AppKit  
**Kind**: method

A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, and the `bottomRadius` uniformly to the bottom-left and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class func uniformEdges(topRadius: NSViewCornerRadius, bottomRadius: NSViewCornerRadius) -> NSViewCornerConfiguration
```

## Parameters

- `topRadius`: Radius for top edge.
- `bottomRadius`: Radius for the bottom edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration/uniformedges(topradius:bottomradius:))*