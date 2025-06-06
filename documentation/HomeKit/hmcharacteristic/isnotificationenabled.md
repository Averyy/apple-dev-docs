# isNotificationEnabled

**Framework**: HomeKit  
**Kind**: property

A Boolean indicating whether the characteristic has been set to send notifications.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isNotificationEnabled: Bool { get }
```

#### Discussion

HomeKit delivers notifications to the accessory delegate using the [`accessory(_:service:didUpdateValueFor:)`](hmaccessorydelegate/accessory(_:service:didupdatevaluefor:).md) method.

## See Also

- [func enableNotification(Bool, completionHandler: ((any Error)?) -> Void)](hmcharacteristic/enablenotification(_:completionhandler:).md)
  Enables or disables notifications for changes in the value of the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/isnotificationenabled)*