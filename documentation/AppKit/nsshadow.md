# NSShadow

**Framework**: AppKit  
**Kind**: class

An object you use to specify attributes to create and style a drop shadow during drawing operations.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSShadow
```

#### Overview

When you create shadows, the system draws them in the default user coordinate space, where coordinates are independent from the pixel values of any particular device. Rotations, translations, and other transformations of the current transformation matrix (CTM) don’t affect the shadow or the apparent position of the shadow’s light source.

A shadow has two positional parameters: an x-offset and a y-offset. Express these values with a single size data type ([`CGSize`](https://developer.apple.com/documentation/CoreFoundation/CGSize) in iOS, [`NSSize`](https://developer.apple.com/documentation/Foundation/NSSize) in macOS), using the units of the default user coordinate space. Positive values for these offsets extend down and to the right from the user’s perspective.

In addition to its positional parameters, a shadow also contains a blur radius, which specifies how much the system blurs a drawn object’s image mask before compositing the image onto the destination. A value of `0` produces no blur. Larger values produce an increasingly large blurred shadow.

You can use an [`NSShadow`](nsshadow.md) object in one of two ways. First, you can set it, like a color or a font, where `NSShadow` attributes apply to everything you draw until you apply another shadow or restore a previous graphics state. Second, you can use an `NSShadow` instance as the value for the [`shadow`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/shadow) text attribute, so the system applies the shadow to the glyphs corresponding to the characters bearing this attribute.

## Topics

### Creating a shadow
- [init()](nsshadow/init.md)
  Creates a shadow object with default values.
### Managing a shadow
- [var shadowOffset: NSSize](nsshadow/shadowoffset.md)
  The shadow’s relative position, which you specify with horizontal and vertical offset values.
- [var shadowBlurRadius: CGFloat](nsshadow/shadowblurradius.md)
  The blur radius of the shadow.
- [var shadowColor: NSColor?](nsshadow/shadowcolor.md)
  The color of the shadow.
### Setting a shadow
- [func set()](nsshadow/set.md)
  Sets the shadow of subsequent drawing operations to the current shadow.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsshadow)*