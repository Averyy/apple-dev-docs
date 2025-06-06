# GCVirtualController.ElementConfiguration

**Framework**: Game Controller  
**Kind**: class

The properties of a virtual controller’s element that you can customize.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class ElementConfiguration
```

## Topics

### Configuring elements
- [var path: UIBezierPath?](gcvirtualcontroller/elementconfiguration/path.md)
  The Bezier path for the shape of an element.
- [var isHidden: Bool](gcvirtualcontroller/elementconfiguration/ishidden.md)
  A Boolean value that determines whether the virtual controller hides the element.
- [var actsAsTouchpad: Bool](gcvirtualcontroller/elementconfiguration/actsastouchpad.md)
  A Boolean value that determines whether the thumbstick element behaves as a touchpad.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func updateConfiguration(forElement: String, configuration: (GCVirtualController.ElementConfiguration) -> GCVirtualController.ElementConfiguration)](gcvirtualcontroller/updateconfiguration(forelement:configuration:).md)
  Changes the configuration for one of the virtual controller’s input elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/elementconfiguration)*