# TKTokenDriver.Configuration

**Framework**: CryptoTokenKit  
**Kind**: class

A configuration for one class of token.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class Configuration
```

## Topics

### Reporting Configuration Information
- [var classID: TKTokenDriver.ClassID](tktokendriver/configuration/classid.md)
  The class identifier of the token driver.
- [var tokenConfigurations: [TKToken.InstanceID : TKToken.Configuration]](tktokendriver/configuration/tokenconfigurations.md)
  A dictionary of all currently configured tokens for this token class, which the token instance identifier keys.
- [class var driverConfigurations: [TKTokenDriver.ClassID : TKTokenDriver.Configuration]](tktokendriver/configuration/driverconfigurations.md)
  A dictionary of token class configurations which the class identifier of the token driver keys.
### Adding and Removing Configurations
- [func addTokenConfiguration(for: TKToken.InstanceID) -> TKToken.Configuration](tktokendriver/configuration/addtokenconfiguration(for:).md)
  Creates a configuration object for a token with the token instance identifier you specify.
- [func removeTokenConfiguration(for: TKToken.InstanceID)](tktokendriver/configuration/removetokenconfiguration(for:).md)
  Removes a configuration for a token with the token instance identifier you specify.

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

- [var delegate: (any TKTokenDriverDelegate)?](tktokendriver/delegate.md)
  The token driver delegate.
- [protocol TKTokenDriverDelegate](tktokendriverdelegate.md)
  The interface that a token driver delegate implements to respond to token creation events.
- [TKTokenDriver.ClassID](tktokendriver/classid.md)
  The type of the class identifier for the token driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver/configuration)*