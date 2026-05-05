# AccessoryFeature

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that defines a capability for an accessory data provider extension.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
protocol AccessoryFeature : Sendable, AppExtensionPoint.Capability
```

#### Overview

Implement this protocol to create a custom capability that your extension supports. Each feature has an associated handler type that processes events for that capability.

## Topics

### Identifying the feature
- [static var featureID: String](accessoryfeature/featureid.md)
  A string identifier for the feature.

## Relationships

### Inherits From
- [AppExtensionPoint.Capability](../ExtensionFoundation/AppExtensionPoint/Capability.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct TransportMessage](transportmessage.md)
  A structure that represents a message for transmission between the system and an accessory.
- [struct SecurityMessage](securitymessage.md)
  A structure that carries key material for negotiating a secure channel between the system and an accessory.
- [enum AccessoryTransport](accessorytransport.md)
  Supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeature)*