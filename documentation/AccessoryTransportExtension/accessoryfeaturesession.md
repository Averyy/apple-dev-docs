# AccessoryFeatureSession

**Framework**: Accessory Transport Extension  
**Kind**: protocol

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
protocol AccessoryFeatureSession : Sendable
```

## Topics

### Instance Properties
- [var sessionID: UUID](accessoryfeaturesession/sessionid.md)
  The session identifier for this capability session.
### Instance Methods
- [func send(message: AccessoryMessage) async throws](accessoryfeaturesession/send(message:).md)
  Send a message to the Transport Extension.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesession)*