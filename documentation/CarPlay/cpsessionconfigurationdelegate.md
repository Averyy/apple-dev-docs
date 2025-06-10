# CPSessionConfigurationDelegate

**Framework**: CarPlay  
**Kind**: protocol

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

## Topics

### Handling Content Style Changes
- [func sessionConfiguration(CPSessionConfiguration, contentStyleChanged: CPContentStyle)](cpsessionconfigurationdelegate/sessionconfiguration(_:contentstylechanged:).md)
  Tells the delegate that the vehicle changed its selected content style.
### Handling Limit Changes
- [func sessionConfiguration(CPSessionConfiguration, limitedUserInterfacesChanged: CPLimitableUserInterface)](cpsessionconfigurationdelegate/sessionconfiguration(_:limiteduserinterfaceschanged:).md)
  Tells the delegate that the system changed keyboard or list limits on the user interface.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(delegate: any CPSessionConfigurationDelegate)](cpsessionconfiguration/init(delegate:).md)
  Creates a session configuration with a delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfigurationdelegate)*