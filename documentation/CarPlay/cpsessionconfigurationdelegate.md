# CPSessionConfigurationDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

Methods you use to respond to changes in the CarPlay environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
protocol CPSessionConfigurationDelegate : NSObjectProtocol
```

```objc
@protocol CPSessionConfigurationDelegate <NSObject>
```

## Overview

Implement this protocol in the custom delegate object you create and assign to a [`CPSessionConfiguration`](./cpsessionconfiguration.md) object. When the CarPlay environment changes, the session configuration reports the changes to the methods of this protocol. For example, vehicles typically disable keyboard input when the vehicle starts moving and reenable it when the vehicle parks. Use your implementations of these methods to update your app’s interface.

## Topics

### Handling environmental changes
- [func sessionConfiguration(CPSessionConfiguration, contentStyleChanged: CPContentStyle)](./cpsessionconfigurationdelegate/sessionconfiguration%28_,contentstylechanged%29.md)
  Tells the delegate about changes to the interface’s appearance.
- [func sessionConfiguration(CPSessionConfiguration, limitedUserInterfacesChanged: CPLimitableUserInterface)](./cpsessionconfigurationdelegate/sessionconfiguration%28_,limiteduserinterfaceschanged%29.md)
  Tells the delegate about changes to the availability of interface features.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a session configuration
- [init(delegate: any CPSessionConfigurationDelegate)](./cpsessionconfiguration/init%28delegate%29.md)
  Configures a session configuration with the custom delegate object you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfigurationdelegate)*