# AXBrailleMap

**Framework**: Accessibility  
**Kind**: class

A representation of a two-dimensional braille display.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- macOS 12.1+
- tvOS 15.2+
- visionOS 1.0+
- watchOS 8.2+

## Declaration

```swift
class AXBrailleMap
```

#### Overview

A braille map object represents a two-dimensional braille display that’s connected to the current Apple device. By specifying the dot patterns in the braille map, you can change the content the user experiences. To render the data from the braille map to the display, implement [`AXBrailleMapRenderer`](axbraillemaprenderer.md).

## Topics

### Creating a braille map
- [init?(coder: NSCoder)](axbraillemap/init(coder:).md)
### Getting display dimensions
- [var dimensions: CGSize](axbraillemap/dimensions.md)
  The number of pins in each dimension of the braille display.
### Accessing dots
- [func setHeight(Float, at: CGPoint)](axbraillemap/setheight(_:at:).md)
  Sets the height of an individual pin on the braille display.
- [func height(at: CGPoint) -> Float](axbraillemap/height(at:).md)
  Retrieves the height of an individual pin on the braille display.
- [subscript(CGPoint) -> Float](axbraillemap/subscript(_:).md)
  Accesses the height of an individual pin on the braille display.
### Displaying images
- [func present(CGImage)](axbraillemap/present(_:).md)
  Converts the data from the image you specify into the braille map.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [protocol AXBrailleMapRenderer](axbraillemaprenderer.md)
  The interface for providing data for a braille map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbraillemap)*