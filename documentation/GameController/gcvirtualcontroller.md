# GCVirtualController

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

A software emulation of a real controller that you configure specifically for your game.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class GCVirtualController
```

```objc
@interface GCVirtualController : NSObject
```

## Mentions

- [Adding virtual controls to games that support game controllers in iOS](./adding-virtual-controls-to-games-that-support-game-controllers-in-ios.md)

#### Overview

Use a virtual controller to display software controls that you can customize over your game. You create a virtual controller from a configuration where you choose the input elements to display. You can even customize the images for the elements. When you connect the controller to the device, users interact with it similarly to a real controller.

![Screenshot of a virtual controller showing left and right thumbsticks with A and B buttons on the right thumbstick.](https://developer.apple.com/tutorials/images/com.apple.gamecontroller/media-3830787@2x.png)

To add a virtual controller to your game, create a [`GCVirtualController.Configuration`](./gcvirtualcontroller/configuration.md) object containing the elements you want to appear in the controller. Then create the virtual controller by passing the configuration to the [`init(configuration:)`](./gcvirtualcontroller/init%28configuration%29.md) method. Use the [`connect(replyHandler:)`](./gcvirtualcontroller/connect%28replyhandler%29.md) method to display the virtual controller on the screen.

To customize an element in the virtual controller, pass a new [`GCVirtualController.ElementConfiguration`](./gcvirtualcontroller/elementconfiguration.md) object for the element to the [`updateConfiguration(forElement:configuration:)`](./gcvirtualcontroller/updateconfiguration%28forelement,configuration%29.md) method.

You process input from a virtual controller similarly to a real controller. Use the [`controller`](./gcvirtualcontroller/controller.md) property to get the underlying [`GCController`](./gccontroller.md) object. You can either poll the elements of the controller object or set the element’s handlers to get callbacks when their input values change.

## Topics

### Creating virtual controllers
- [init(configuration: GCVirtualController.Configuration)](./gcvirtualcontroller/init%28configuration%29.md)
  Creates a new virtual controller using the configuration you specify.
- [GCVirtualController.Configuration](./gcvirtualcontroller/configuration.md)
  The configuration of a virtual controller.
### Customizing the elements
- [func updateConfiguration(forElement: String, configuration: (GCVirtualController.ElementConfiguration) -> GCVirtualController.ElementConfiguration)](./gcvirtualcontroller/updateconfiguration%28forelement,configuration%29.md)
  Changes the configuration for one of the virtual controller’s input elements.
- [GCVirtualController.ElementConfiguration](./gcvirtualcontroller/elementconfiguration.md)
  The properties of a virtual controller’s element that you can customize.
### Accessing the elements
- [var controller: GCController?](./gcvirtualcontroller/controller.md)
  The underlying controller object that you use to access input elements.
### Connecting and displaying virtual controllers
- [func connect(replyHandler: (((any Error)?) -> Void)?)](./gcvirtualcontroller/connect%28replyhandler%29.md)
  Connects the virtual controller to the device and displays it on the screen.
- [func disconnect()](./gcvirtualcontroller/disconnect%28%29.md)
  Disconnects the virtual controller from the device and removes it from the screen.
### Presenting a custom interface
- [func setPosition(CGPoint, forDirectionPadElement: String)](./gcvirtualcontroller/setposition%28_,fordirectionpadelement%29.md)
  Changes the value of a directional pad element in the virtual controller.
- [func setValue(CGFloat, forButtonElement: String)](./gcvirtualcontroller/setvalue%28_,forbuttonelement%29.md)
  Changes the value of a button element in the virtual controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Virtual controller
- [Adding virtual controls to games that support game controllers in iOS](./adding-virtual-controls-to-games-that-support-game-controllers-in-ios.md)
  Use touch input and virtual controllers to make your game available to players without controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller)*