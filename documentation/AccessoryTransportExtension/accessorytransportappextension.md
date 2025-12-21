# AccessoryTransportAppExtension

**Framework**: AccessoryTransportExtension  
**Kind**: protocol

A protocol that defines the behavior of the app extension and how it handles requests.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
protocol AccessoryTransportAppExtension : AppExtension
```

## Topics

### Interacting with a session
- [func accept(sessionRequest: AccessoryTransportSession.Request) -> AccessoryTransportSession.Request.Decision](accessorytransportappextension/accept(sessionrequest:).md)
  Handles a new session request for the accessory, in response to a call from the framework.
- [AccessoryTransportSession.Request.Decision](accessorytransportsession/request/decision.md)
  An opaque type returned from the incoming session handler of an event listener.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [protocol AccessoryTransportExtensionConfiguration](accessorytransportextensionconfiguration.md)
  An interface you use to configure and manage communication between the extension and the host process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension)*