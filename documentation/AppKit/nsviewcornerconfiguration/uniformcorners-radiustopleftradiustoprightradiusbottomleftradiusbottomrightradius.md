# uniformCorners(radius:topLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:)

**Framework**: AppKit  
**Kind**: method

A configuration that applies the given uniform radius uniformly to all corners that are otherwise unspecified. Any specified corner is independent of the others.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class func uniformCorners(radius: NSViewCornerRadius, topLeftRadius: NSViewCornerRadius?, topRightRadius: NSViewCornerRadius?, bottomLeftRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration
```

## Parameters

- `radius`: Uniform radius for all unspecified corners.
- `topLeftRadius`: Radius of top left corner.
- `topRightRadius`: Radius of top right corner.
- `bottomLeftRadius`: Radius of bottom left corner.
- `bottomRightRadius`: Radius of bottom right corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration/uniformcorners(radius:topleftradius:toprightradius:bottomleftradius:bottomrightradius:))*