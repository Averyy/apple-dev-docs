# CPSessionConfiguration

**Framework**: CarPlay  
**Kind**: class

An object that provides vehicle properties and configuration for the CarPlay environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPSessionConfiguration
```

#### Overview

You use a session configuration to determine any user interface limits the vehicle imposes, such as keyboard display and list length, and the content style the vehicle selects according to the ambient light level.

## Topics

### Creating a Session Configuration
- [init(delegate: any CPSessionConfigurationDelegate)](cpsessionconfiguration/init(delegate:).md)
  Creates a session configuration with a delegate.
- [protocol CPSessionConfigurationDelegate](cpsessionconfigurationdelegate.md)
  A protocol for receiving notifications about changes to vehicle properties and configuration.
### Managing the Delegate
- [var delegate: (any CPSessionConfigurationDelegate)?](cpsessionconfiguration/delegate.md)
  An object that serves as the delegate to the session configuration.
### Getting the Content Style
- [var contentStyle: CPContentStyle](cpsessionconfiguration/contentstyle.md)
  The content style that the vehicle selects.
- [struct CPContentStyle](cpcontentstyle.md)
  The types of content style that the vehicle allows.
### Getting the Limits
- [var limitedUserInterfaces: CPLimitableUserInterface](cpsessionconfiguration/limiteduserinterfaces.md)
  A bit mask value that indicates the user interface limits.
- [struct CPLimitableUserInterface](cplimitableuserinterface.md)
  The types of limitable user interface elements.

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

- [Requesting CarPlay Entitlements](requesting-carplay-entitlements.md)
  Configure your CarPlay-enabled app with the entitlements it requires.
- [Displaying Content in CarPlay](displaying-content-in-carplay.md)
  Use scenes to present your app’s content on the vehicle’s built-in screen.
- [Supporting Previous Versions of iOS](supporting-previous-versions-of-ios.md)
  Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.
- [Using the CarPlay Simulator](using-the-carplay-simulator.md)
  Configure Simulator to run and debug your CarPlay-enabled app.
- [class CPTemplateApplicationScene](cptemplateapplicationscene.md)
  A CarPlay scene that controls your app’s user interface.
- [protocol CPTemplateApplicationSceneDelegate](cptemplateapplicationscenedelegate.md)
  The methods for responding to the life cycle events of your app’s scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfiguration)*