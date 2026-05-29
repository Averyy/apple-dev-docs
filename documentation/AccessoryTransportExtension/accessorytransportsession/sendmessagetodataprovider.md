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

> **Note**: This method receives data from the accessory for the Bluetooth transport type; internet transport accessory-to-host communication relies on a different delivery mechanism.

## Parameters

- `message`: A transport message to send to the data provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/sendmessagetodataprovider(_:))*