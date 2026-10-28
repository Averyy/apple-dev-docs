# isNotificationEnabled

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isNotificationEnabled) BOOL notificationEnabled;
```

## Discussion

HomeKit delivers notifications to the accessory delegate using the [`accessory(_:service:didUpdateValueFor:)`](../hmaccessorydelegate/accessory%28_,service,didupdatevaluefor%29.md) method.

## See Also

### Receiving change notifications
- [func enableNotification(Bool, completionHandler: ((any Error)?) -> Void)](./enablenotification%28_,completionhandler%29.md)
  Enables or disables notifications for changes in the value of the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/isnotificationenabled)*