# NSViewCornerConfiguration

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A configuration object that defines the corner styles of a view’s overall shape.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class NSViewCornerConfiguration
```

```objc
@interface NSViewCornerConfiguration : NSObject
```

## Topics

### Type Properties
- [class var capsule: NSViewCornerConfiguration](./nsviewcornerconfiguration/capsule.md)
  A configuration where the container is to take on a capsule shape, scaling with the view’s size.
### Type Methods
- [class func capsule(maximumRadius: CGFloat) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/capsule%28maximumradius%29.md)
  A configuration where the container is to take on a capsule shape, scaling with the view’s size. and clamped to the `maximumRadius`.
- [class func corners(radius: NSViewCornerRadius) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/corners%28radius%29.md)
  A configuration that applies the given radius independently to all corners.
- [class func corners(topLeftRadius: NSViewCornerRadius?, topRightRadius: NSViewCornerRadius?, bottomLeftRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/corners%28topleftradius,toprightradius,bottomleftradius,bottomrightradius%29.md)
  A configuration with independent radii for each corner.
- [class func uniformBottomRadius(NSViewCornerRadius, topLeftRadius: NSViewCornerRadius?, topRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/uniformbottomradius%28_,topleftradius,toprightradius%29.md)
  A configuration that applies the `bottomRadius` uniformly to the bottom-left and bottom-right corners, with optional independent radii for the top-left and top-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformCorners(radius: NSViewCornerRadius) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/uniformcorners%28radius%29.md)
  A configuration that applies the given radius uniformly to all corners, using the largest of the resolved corner radii when they differ.
- [class func uniformCorners(radius: NSViewCornerRadius, topLeftRadius: NSViewCornerRadius?, topRightRadius: NSViewCornerRadius?, bottomLeftRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/uniformcorners%28radius,topleftradius,toprightradius,bottomleftradius,bottomrightradius%29.md)
  A configuration that applies the given uniform radius uniformly to all corners that are otherwise unspecified. Any specified corner is independent of the others.
- [class func uniformEdges(leftRadius: NSViewCornerRadius, rightRadius: NSViewCornerRadius) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/uniformedges%28leftradius,rightradius%29.md)
  A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, and the `rightRadius` uniformly to the top-right and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformEdges(topRadius: NSViewCornerRadius, bottomRadius: NSViewCornerRadius) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/uniformedges%28topradius,bottomradius%29.md)
  A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, and the `bottomRadius` uniformly to the bottom-left and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformLeftRadius(NSViewCornerRadius, topRightRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/uniformleftradius%28_,toprightradius,bottomrightradius%29.md)
  A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, with optional independent radii for the top-right and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformRightRadius(NSViewCornerRadius, topLeftRadius: NSViewCornerRadius?, bottomLeftRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/uniformrightradius%28_,topleftradius,bottomleftradius%29.md)
  A configuration that applies the `rightRadius` uniformly to the top-right and bottom-right corners, with optional independent radii for the top-left and bottom-left corners. When the uniform corners differ, it uses the largest of the resolved corner radii.
- [class func uniformTopRadius(NSViewCornerRadius, bottomLeftRadius: NSViewCornerRadius?, bottomRightRadius: NSViewCornerRadius?) -> NSViewCornerConfiguration](./nsviewcornerconfiguration/uniformtopradius%28_,bottomleftradius,bottomrightradius%29.md)
  A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, with optional independent radii for the bottom-left and bottom-right corners. When the uniform corners differ, it uses the largest of the resolved corner radii.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Corner configuration
- [class NSViewCornerRadii](./nsviewcornerradii.md)
  Provides a structured way to define custom corner radii for each corner of a view, along with a corner curve.
- [class NSViewCornerRadius](./nsviewcornerradius.md)
  Represents a radius used to round a corner. It supports fixed and adaptive configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration)*