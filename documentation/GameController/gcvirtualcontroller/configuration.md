# GCVirtualController.Configuration

**Framework**: Game Controller  
**Kind**: class

The configuration of a virtual controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class Configuration
```

## Mentions

- [Adding touch controls to games that support game controllers in iOS](adding-touch-controls-to-games-that-support-game-controllers-in-ios.md)

#### Overview

You configure a virtual controller by specifying the input elements it contains. Then using the [`updateConfiguration(forElement:configuration:)`](gcvirtualcontroller/updateconfiguration(forelement:configuration:).md) method, you can customize individual elements.

## Topics

### Setting the elements
- [var elements: Set<String>](gcvirtualcontroller/configuration/elements.md)
  The input elements of a virtual controller.
### Presenting a custom interface
- [var isHidden: Bool](gcvirtualcontroller/configuration/ishidden.md)
  A Boolean value that indicates whether the system or the app presents the virtual interface.

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

- [init(configuration: GCVirtualController.Configuration)](gcvirtualcontroller/init(configuration:).md)
  Creates a new virtual controller using the configuration you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/configuration)*