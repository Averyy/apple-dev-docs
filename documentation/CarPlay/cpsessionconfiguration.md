# CPSessionConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

An object that keeps you informed of changes to the CarPlay environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPSessionConfiguration
```

```objc
@interface CPSessionConfiguration : NSObject
```

## Overview

A `CPSessionConfiguration` object provides your app with the current configuration of the CarPlay environment. When building a CarPlay app, use the information in this object to make decisions about what content to display and how to display it. For example, you might disable your app’s video features if the [`supportsVideoPlayback`](./cpsessionconfiguration/supportsvideoplayback.md) property is `false`.

Create an instance of `CPSessionConfiguration` when your app starts and use it to get the current values. When instantiating this type, you also provide a custom delegate object to respond to subsequent environment changes. Define this type in your code and use the methods of the [`CPSessionConfigurationDelegate`](./cpsessionconfigurationdelegate.md) protocol to receive the updated values. Keep a strong reference to the `CPSessionConfiguration` object and your custom delegate object while your app runs.

## Topics

### Creating a session configuration
- [init(delegate: any CPSessionConfigurationDelegate)](./cpsessionconfiguration/init%28delegate%29.md)
  Configures a session configuration with the custom delegate object you provide.
- [protocol CPSessionConfigurationDelegate](./cpsessionconfigurationdelegate.md)
  Methods you use to respond to changes in the CarPlay environment.
### Responding to configuration changes
- [var delegate: (any CPSessionConfigurationDelegate)?](./cpsessionconfiguration/delegate.md)
  The custom object you use to handle changes to environment values.
### Getting the configuration details
- [var contentStyle: CPContentStyle](./cpsessionconfiguration/contentstyle.md)
  The preferred interface style for your app’s content.
- [var limitedUserInterfaces: CPLimitableUserInterface](./cpsessionconfiguration/limiteduserinterfaces.md)
  A bitmask of the interface restrictions that currently apply to your app.
- [var supportsVideoPlayback: Bool](./cpsessionconfiguration/supportsvideoplayback.md)
  A Boolean value that indicates whether CarPlay supports playing video content.
- [struct CPContentStyle](./cpcontentstyle.md)
  The types of content style that the vehicle allows.
- [struct CPLimitableUserInterface](./cplimitableuserinterface.md)
  The types of interfaces to which a vehicle can limit access.

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

### App management
- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)
  Build the interface for your CarPlay app using scenes and templates from the CarPlay framework.
- [class CPTemplateApplicationScene](./cptemplateapplicationscene.md)
  A CarPlay scene that manages your app’s interface on the vehicle’s center display.
- [protocol CPTemplateApplicationSceneDelegate](./cptemplateapplicationscenedelegate.md)
  Methods for responding to  life-cycle events in your app’s scene.
- [class CPInterfaceController](./cpinterfacecontroller.md)
  The type you use to present your app’s CarPlay interface and change what appears on the vehicle’s display.
- [class CPWindow](./cpwindow.md)
  A type that navigation apps use to present their map content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfiguration)*