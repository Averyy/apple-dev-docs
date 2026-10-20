# GCVirtualController.ElementConfiguration

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

The properties of a virtual controller’s element that you can customize.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class ElementConfiguration
```

```objc
@interface GCVirtualControllerElementConfiguration : NSObject
```

## Topics

### Configuring elements
- [var path: UIBezierPath?](./elementconfiguration/path.md)
  The Bezier path for the shape of an element.
- [var isHidden: Bool](./elementconfiguration/ishidden.md)
  A Boolean value that determines whether the virtual controller hides the element.
- [var actsAsTouchpad: Bool](./elementconfiguration/actsastouchpad.md)
  A Boolean value that determines whether the thumbstick element behaves as a touchpad.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Customizing the elements
- [func updateConfiguration(forElement: String, configuration: (GCVirtualController.ElementConfiguration) -> GCVirtualController.ElementConfiguration)](./updateconfiguration%28forelement,configuration%29.md)
  Changes the configuration for one of the virtual controller’s input elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/elementconfiguration)*