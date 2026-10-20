# GCColor

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

The color of a device light.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCColor
```

```objc
@interface GCColor : NSObject
```

## Topics

### Creating colors
- [init(red: Float, green: Float, blue: Float)](./gccolor/init%28red,green,blue%29.md)
  Creates a color with the specified red, green, and blue values.
### Setting color values
- [var red: Float](./gccolor/red.md)
  The normalized value of the red component ranging from 0 to 1.
- [var green: Float](./gccolor/green.md)
  The normalized value of the green component ranging from 0 to 1.
- [var blue: Float](./gccolor/blue.md)
  The normalized value of the blue component ranging from 0 to 1.
### Initializers
- [init?(coder: NSCoder)](./gccolor/init%28coder%29.md)

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

### Getting the light’s color
- [var color: GCColor](./gcdevicelight/color.md)
  The color of a device’s light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccolor)*