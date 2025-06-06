# enableNotification(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Enables or disables notifications for changes in the value of the characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enableNotification(_ enable: Bool) async throws
```

#### Discussion

HomeKit delivers notifications to the accessory delegate using the [`accessory(_:service:didUpdateValueFor:)`](hmaccessorydelegate/accessory(_:service:didupdatevaluefor:).md) method.

## Parameters

- `enable`:   to enable notifications,   to disable notifications.
- `completion`: The block executed after the request is processed.

## See Also

- [var isNotificationEnabled: Bool](hmcharacteristic/isnotificationenabled.md)
  A Boolean indicating whether the characteristic has been set to send notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/enablenotification(_:completionhandler:))*