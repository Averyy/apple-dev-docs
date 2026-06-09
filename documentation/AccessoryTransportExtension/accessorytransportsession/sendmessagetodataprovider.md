# sendMessageToDataProvider(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Sends a message to the data provider extension.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
func sendMessageToDataProvider(_ message: TransportMessage) throws(AccessoryTransportSession.Error)
```

#### Discussion

Use this method to relay data from the accessory to your app’s [`AccessoryDataProvider`](accessorydataprovider.md) extension. The system decrypts the message, if necessary, before delivering it to the data provider. Data providers receive the message through [`messageHandler(_:)`](https://developer.apple.com/documentation/AccessoryNotifications/NotificationsForwarding/AccessoryNotificationsHandler/messageHandler(_:)).

> **Note**: This method relays data from the accessory for the Bluetooth transport type. For internet transport, the accessory routes its response to the device using [`pushToken`](accessorytransportsession/pushtoken.md); the system delivers the decrypted response to your data provider extension through the same message handler.

## Parameters

- `message`: A transport message to send to the data provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/sendmessagetodataprovider(_:))*