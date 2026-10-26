# GCVirtualController.Configuration

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

The configuration of a virtual controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class Configuration
```

```objc
@interface GCVirtualControllerConfiguration : NSObject
```

## Mentions

- [Adding virtual controls to games that support game controllers in iOS](../adding-virtual-controls-to-games-that-support-game-controllers-in-ios.md)

#### Overview

You configure a virtual controller by specifying the input elements it contains. Then using the [`updateConfiguration(forElement:configuration:)`](./updateconfiguration%28forelement,configuration%29.md) method, you can customize individual elements.

## Topics

### Setting the elements
- [var elements: Set<String>](./configuration/elements.md)
  The input elements of a virtual controller.
### Presenting a custom interface
- [var isHidden: Bool](./configuration/ishidden.md)
  A Boolean value that indicates whether the system or the app presents the virtual interface.

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

### Creating virtual controllers
- [init(configuration: GCVirtualController.Configuration)](./init%28configuration%29.md)
  Creates a new virtual controller using the configuration you specify.
- [+ virtualControllerWithConfiguration:](./virtualcontrollerwithconfiguration_.md)
  Creates a new virtual controller using the configuration you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/configuration)*