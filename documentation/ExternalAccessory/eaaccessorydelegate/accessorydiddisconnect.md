# accessoryDidDisconnect(_:)

**Framework**: External Accessory  
**Kind**: method

Tells the delegate that the specified accessory was disconnected from the device.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func accessoryDidDisconnect(_ accessory: EAAccessory)
```

#### Discussion

The accessory manager calls this method as a convenience whenever it receives an [`EAAccessoryDidDisconnectNotification`](eaaccessorydiddisconnectnotification.md) notification. You can use this method to remove any references to the specified accessory object and to stop any services currently using the accessory.

Because this is a convenience method, your delegate does not also need to register as an observer of the [`EAAccessoryDidDisconnectNotification`](eaaccessorydiddisconnectnotification.md) notification. However, if you want your delegate to be notified of newly connected accessories, you should configure it as an observer of the [`EAAccessoryDidConnectNotification`](eaaccessorydidconnectnotification.md) notification.

## Parameters

- `accessory`: The accessory that was disconnected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessorydelegate/accessorydiddisconnect(_:))*