# NSViewCornerRadius

**Framework**: AppKit  
**Kind**: class

Represents a radius used to round a corner. It supports fixed and adaptive configurations.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
class NSViewCornerRadius
```

## Topics

### Type Properties
- [class var containerConcentric: NSViewCornerRadius](nsviewcornerradius/containerconcentric.md)
  A dynamic corner radius calculated based on the view’s container shape.
### Type Methods
- [class func containerConcentric(CGFloat) -> NSViewCornerRadius](nsviewcornerradius/containerconcentric(_:).md)
  A dynamic corner radius calculated based on the view’s container shape and limited to the provided minimum radius.
- [class func fixed(CGFloat) -> NSViewCornerRadius](nsviewcornerradius/fixed(_:).md)
  Shorthand initializer for a configuration where all four corners are using a fixed corner radius in points.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSViewCornerConfiguration](nsviewcornerconfiguration.md)
  A configuration object that defines the corner styles of a view’s overall shape.
- [class NSViewCornerRadii](nsviewcornerradii.md)
  Provides a structured way to define custom corner radii for each corner of a view, along with a corner curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerradius)*