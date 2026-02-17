# AccessoryFeature

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that defines a capability for an accessory data provider extension.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
protocol AccessoryFeature : Sendable, AppExtensionPoint.Capability
```

#### Overview

Implement this protocol to create a custom capability that your extension supports. Each feature has an associated handler type that processes events for that capability.

## Topics

### Creating an accessory feature
- [init(Self.HandlerFactory)](accessoryfeature/init(_:).md)
  Initializes a feature with a handler factory closure.
### Identifying the feature
- [static var featureID: String](accessoryfeature/featureid.md)
  A string identifier for the feature.
### Creating a handler
- [associatedtype Handler](accessoryfeature/handler.md)
  An associated type that defines the handler for this feature.
- [AccessoryFeature.HandlerFactory](accessoryfeature/handlerfactory.md)
  A type alias for a factory closure that creates feature handlers.

## Relationships

### Inherits From
- [AppExtensionPoint.Capability](../ExtensionFoundation/AppExtensionPoint/Capability.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AccessoryFeatureSession](accessoryfeaturesession.md)
  A protocol that manages a session for a specific feature capability.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct AccessorySecurity](accessorysecurity.md)
  Types of security events and cryptography operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeature)*