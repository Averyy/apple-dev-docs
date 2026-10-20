# NSViewCornerRadius

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

Represents a radius used to round a corner. It supports fixed and adaptive configurations.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class NSViewCornerRadius
```

```objc
@interface NSViewCornerRadius : NSObject
```

## Topics

### Type Properties
- [class var containerConcentric: NSViewCornerRadius](./nsviewcornerradius/containerconcentric.md)
  A dynamic corner radius calculated based on the view’s container shape.
### Type Methods
- [class func containerConcentric(CGFloat) -> NSViewCornerRadius](./nsviewcornerradius/containerconcentric%28_%29.md)
  A dynamic corner radius calculated based on the view’s container shape and limited to the provided minimum radius.
- [class func fixed(CGFloat) -> NSViewCornerRadius](./nsviewcornerradius/fixed%28_%29.md)
  Shorthand initializer for a configuration where all four corners are using a fixed corner radius in points.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Corner configuration
- [class NSViewCornerConfiguration](./nsviewcornerconfiguration.md)
  A configuration object that defines the corner styles of a view’s overall shape.
- [class NSViewCornerRadii](./nsviewcornerradii.md)
  Provides a structured way to define custom corner radii for each corner of a view, along with a corner curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerradius)*