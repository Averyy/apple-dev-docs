# corners(topLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

A configuration with independent radii for each corner.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class func corners(topLeftRadius: NSViewCornerRadius?, topRightRadius: NSViewCornerRadius?, bottomLeftRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration
```

```objc
+ (NSViewCornerConfiguration *) configurationWithTopLeftRadius:(NSViewCornerRadius *) topLeftRadius topRightRadius:(NSViewCornerRadius *) topRightRadius bottomLeftRadius:(NSViewCornerRadius *) bottomLeftRadius bottomRightRadius:(NSViewCornerRadius *) bottomRightRadius;
```

## Parameters

- `topLeftRadius`: Radius of top left corner.
- `topRightRadius`: Radius of top right corner.
- `bottomLeftRadius`: Radius of bottom left corner.
- `bottomRightRadius`: Radius of bottom right corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration/corners(topleftradius:toprightradius:bottomleftradius:bottomrightradius:))*