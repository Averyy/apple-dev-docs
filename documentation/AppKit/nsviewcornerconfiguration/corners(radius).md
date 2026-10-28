# corners(radius:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

A configuration that applies the given radius independently to all corners.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class func corners(radius: NSViewCornerRadius) -> NSViewCornerConfiguration
```

```objc
+ (NSViewCornerConfiguration *) configurationWithRadius:(NSViewCornerRadius *) radius;
```

## Discussion

When used with a container concentric radius, this allows each individual corner to resolve to different radii.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration/corners(radius:))*