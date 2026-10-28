# AXBrailleMap

**Framework**: Accessibility  
**Kind**: class  
**Role**: Class

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

```objc
@interface AXBrailleMap : NSObject
```

## Overview

A braille map object represents a two-dimensional braille display that’s connected to the current Apple device. By specifying the dot patterns in the braille map, you can change the content the user experiences. To render the data from the braille map to the display, implement [`AXBrailleMapRenderer`](./axbraillemaprenderer.md).

## Topics

### Creating a braille map
- [init?(coder: NSCoder)](./axbraillemap/init%28coder%29.md)
### Getting display dimensions
- [var dimensions: CGSize](./axbraillemap/dimensions.md)
  The number of pins in each dimension of the braille display.
### Accessing dots
- [func setHeight(Float, at: CGPoint)](./axbraillemap/setheight%28_,at%29.md)
  Sets the height of an individual pin on the braille display.
- [func height(at: CGPoint) -> Float](./axbraillemap/height%28at%29.md)
  Retrieves the height of an individual pin on the braille display.
- [subscript(CGPoint) -> Float](./axbraillemap/subscript%28_%29.md)
  Accesses the height of an individual pin on the braille display.
### Displaying images
- [func present(CGImage)](./axbraillemap/present%28_%29.md)
  Converts the data from the image you specify into the braille map.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Braille maps
- [protocol AXBrailleMapRenderer](./axbraillemaprenderer.md)
  The interface for providing data for a braille map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbraillemap)*