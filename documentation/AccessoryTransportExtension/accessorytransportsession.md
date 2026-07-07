# AccessoryTransportSession

**Framework**: Accessory Transport Extension  
**Kind**: class

A class that manages a transport session between the extension and the system.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
class AccessoryTransportSession
```

#### Overview

The [`AccessoryTransportAppExtension`](accessorytransportappextension.md) protocol’s [`accept(sessionRequest:)`](accessorytransportappextension/accept(sessionrequest:).md) method receives a [`AccessoryTransportSession.Request`](accessorytransportsession/request.md) object containing an instance of this class.

## Topics

### Managing session requests
- [AccessoryTransportSession.Request](accessorytransportsession/request.md)
  An incoming session request that your extension accepts or rejects.
### Handling session events
- [AccessoryTransportSession.EventHandler](accessorytransportsession/eventhandler.md)
  A protocol that defines methods for handling transport session events.
- [AccessoryTransportSession.DataEvent](accessorytransportsession/dataevent.md)
  An enumeration of data events that the transport extension receives.
### Managing the session life cycle
- [func cancel(error: AccessoryTransportSession.Error?)](accessorytransportsession/cancel(error:).md)
  Cancels the session.
### Accessing session properties
- [var description: String](accessorytransportsession/description.md)
  A string that describes the transport session.
### Sending data
- [func sendMessageToDataProvider(TransportMessage) throws(AccessoryTransportSession.Error)](accessorytransportsession/sendmessagetodataprovider(_:).md)
  Sends a message to the data provider extension.
### Handling errors
- [AccessoryTransportSession.Error](accessorytransportsession/error.md)
  Errors that can occur with an accessory transport session.
### Determining the communication method
- [var transport: AccessoryTransport?](accessorytransportsession/transport.md)
  A transport method that the session uses to communicate with the accessory.
- [var transportStateRestoreIdentifier: String?](accessorytransportsession/transportstaterestoreidentifier.md)
  An optional identifier for restoring transport state across sessions.
- [var pushToken: Data?](accessorytransportsession/pushtoken.md)
  A token that identifies the iOS device to the Apple Push Notification service for routing accessory responses over the internet.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [protocol AccessoryTransportAppExtension](accessorytransportappextension.md)
  A protocol for an extension that transmits data to an accessory you develop.
- [protocol AccessoryTransportExtensionConfiguration](accessorytransportextensionconfiguration.md)
  An interface that enables you to configure and manage communication between your extension and the system.
- [Wi-Fi Infrastructure](../WiFiInfrastructure/WiFiInfrastructure.md)
  Share Wi-Fi network credentials securely between devices and connected accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession)*