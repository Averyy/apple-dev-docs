# NSViewCornerConfiguration

**Framework**: AppKit  
**Kind**: class

A configuration object that defines the corner styles of a view’s overall shape.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class NSViewCornerConfiguration
```

## Topics

### Type Properties
- [class var capsule: NSViewCornerConfiguration](nsviewcornerconfiguration/capsule.md)
  A configuration where the container is to take on a capsule shape, scaling with the view’s size.
### Type Methods
- [class func capsule(maximumRadius: CGFloat) -> NSViewCornerConfiguration](nsviewcornerconfiguration/capsule(maximumradius:).md)
  A configuration where the container is to take on a capsule shape, scaling with the view’s size. and clamped to the `maximumRadius`.
- [class func corners(radius: NSViewCornerRadius) -> NSViewCornerConfiguration](nsviewcornerconfiguration/corners(radius:).md)
  A configuration that applies the given radius independently to all corners.
- [class func corners(topLeftRadius: NSViewCornerRadius?, topRightRadius: NSViewCornerRadius?, bottomLeftRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](nsviewcornerconfiguration/corners(topleftradius:toprightradius:bottomleftradius:bottomrightradius:).md)
  A configuration with independent radii for each corner.
- [class func uniformBottomRadius(NSViewCornerRadius, topLeftRadius: NSViewCornerRadius?, topRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](nsviewcornerconfiguration/uniformbottomradius(_:topleftradius:toprightradius:).md)
  A configuration that applies the `bottomRadius` uniformly to the bottom-left and bottom-right corners, with optional independent radii for the top-left and top-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformCorners(radius: NSViewCornerRadius) -> NSViewCornerConfiguration](nsviewcornerconfiguration/uniformcorners(radius:).md)
  A configuration that applies the given radius uniformly to all corners, using the largest of the resolved corner radii when they differ.
- [class func uniformCorners(radius: NSViewCornerRadius, topLeftRadius: NSViewCornerRadius?, topRightRadius: NSViewCornerRadius?, bottomLeftRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](nsviewcornerconfiguration/uniformcorners(radius:topleftradius:toprightradius:bottomleftradius:bottomrightradius:).md)
  A configuration that applies the given uniform radius uniformly to all corners that are otherwise unspecified. Any specified corner is independent of the others.
- [class func uniformEdges(leftRadius: NSViewCornerRadius, rightRadius: NSViewCornerRadius) -> NSViewCornerConfiguration](nsviewcornerconfiguration/uniformedges(leftradius:rightradius:).md)
  A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, and the `rightRadius` uniformly to the top-right and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformEdges(topRadius: NSViewCornerRadius, bottomRadius: NSViewCornerRadius) -> NSViewCornerConfiguration](nsviewcornerconfiguration/uniformedges(topradius:bottomradius:).md)
  A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, and the `bottomRadius` uniformly to the bottom-left and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformLeftRadius(NSViewCornerRadius, topRightRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](nsviewcornerconfiguration/uniformleftradius(_:toprightradius:bottomrightradius:).md)
  A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, with optional independent radii for the top-right and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformRightRadius(NSViewCornerRadius, topLeftRadius: NSViewCornerRadius?, bottomLeftRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](nsviewcornerconfiguration/uniformrightradius(_:topleftradius:bottomleftradius:).md)
  A configuration that applies the `rightRadius` uniformly to the top-right and bottom-right corners, with optional independent radii for the top-left and bottom-left corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformTopRadius(NSViewCornerRadius, bottomLeftRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](nsviewcornerconfiguration/uniformtopradius(_:bottomleftradius:bottomrightradius:).md)
  A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, with optional independent radii for the bottom-left and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class NSViewCornerRadii](nsviewcornerradii.md)
  Provides a structured way to define custom corner radii for each corner of a view, along with a corner curve.
- [class NSViewCornerRadius](nsviewcornerradius.md)
  Represents a radius used to round a corner. It supports fixed and adaptive configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration)*