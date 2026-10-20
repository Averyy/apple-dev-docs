# CPSessionConfigurationDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

A protocol for receiving notifications about changes to vehicle properties and configuration.

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

## Topics

### Handling Content Style Changes
- [func sessionConfiguration(CPSessionConfiguration, contentStyleChanged: CPContentStyle)](./cpsessionconfigurationdelegate/sessionconfiguration%28_,contentstylechanged%29.md)
  Tells the delegate that the vehicle changed its selected content style.
### Handling Limit Changes
- [func sessionConfiguration(CPSessionConfiguration, limitedUserInterfacesChanged: CPLimitableUserInterface)](./cpsessionconfigurationdelegate/sessionconfiguration%28_,limiteduserinterfaceschanged%29.md)
  Tells the delegate that the system changed keyboard or list limits on the user interface.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a Session Configuration
- [init(delegate: any CPSessionConfigurationDelegate)](./cpsessionconfiguration/init%28delegate%29.md)
  Creates a session configuration with a delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfigurationdelegate)*