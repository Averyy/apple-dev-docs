# PKAddCarKeyPassConfiguration

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

A specialized configuration object that PassKit uses when it creates a digital car key.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class PKAddCarKeyPassConfiguration
```

## Topics

### Creating a pass configuration
- [init()](pkaddcarkeypassconfiguration/init.md)
  Creates a digital car key configuration object.
### Setting the wireless radio technology
- [var supportedRadioTechnologies: PKRadioTechnology](pkaddcarkeypassconfiguration/supportedradiotechnologies.md)
  The wireless radio technology that the key uses.
- [struct PKRadioTechnology](pkradiotechnology.md)
  Constants that describe the type of wireless radio technology that a pass uses.
### Managing the password
- [var password: String](pkaddcarkeypassconfiguration/password.md)
  A one-time password that the vehicle manufacturer provides.
### Setting the provisioning template
- [var provisioningTemplateIdentifier: String?](pkaddcarkeypassconfiguration/provisioningtemplateidentifier.md)
### Instance Properties
- [var manufacturerIdentifier: String](pkaddcarkeypassconfiguration/manufactureridentifier.md)

## Relationships

### Inherits From
- [PKAddSecureElementPassConfiguration](pkaddsecureelementpassconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKVehicleConnectionSession](pkvehicleconnectionsession.md)
- [protocol PKVehicleConnectionDelegate](pkvehicleconnectiondelegate.md)
- [enum PKVehicleConnectionSessionConnectionState](pkvehicleconnectionsessionconnectionstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddcarkeypassconfiguration)*