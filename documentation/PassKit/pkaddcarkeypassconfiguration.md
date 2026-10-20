# PKAddCarKeyPassConfiguration

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

A specialized configuration object that PassKit uses when it creates a digital car key.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS
- visionOS 1.0+

## Declaration

```swift
class PKAddCarKeyPassConfiguration
```

```objc
@interface PKAddCarKeyPassConfiguration : PKAddSecureElementPassConfiguration
```

## Topics

### Creating a pass configuration
- [init()](./pkaddcarkeypassconfiguration/init%28%29.md)
  Creates a digital car key configuration object.
### Adding identifiers
- [var manufacturerIdentifier: String?](./pkaddcarkeypassconfiguration/manufactureridentifier.md)
- [var productPlanIdentifier: String?](./pkaddcarkeypassconfiguration/productplanidentifier.md)
  The product plan identifier (PPID) supplied by the vehicle’s original equipment manufacturer (OEM).
### Setting the wireless radio technology
- [var supportedRadioTechnologies: PKRadioTechnology](./pkaddcarkeypassconfiguration/supportedradiotechnologies.md)
  The wireless radio technology that the key uses.
- [struct PKRadioTechnology](./pkradiotechnology.md)
  Constants that describe the type of wireless radio technology that a pass uses.
### Managing the password
- [var password: String](./pkaddcarkeypassconfiguration/password.md)
  A one-time password that the vehicle manufacturer provides.
### Setting the provisioning template
- [var provisioningTemplateIdentifier: String?](./pkaddcarkeypassconfiguration/provisioningtemplateidentifier.md)

## Relationships

### Inherits From
- [PKAddSecureElementPassConfiguration](./pkaddsecureelementpassconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Digital car keys
- [class PKVehicleConnectionSession](./pkvehicleconnectionsession.md)
- [protocol PKVehicleConnectionDelegate](./pkvehicleconnectiondelegate.md)
- [enum PKVehicleConnectionSessionConnectionState](./pkvehicleconnectionsessionconnectionstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddcarkeypassconfiguration)*