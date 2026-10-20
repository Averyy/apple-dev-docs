# enableNotification(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

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
func enableNotification(_ enable: Bool, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func enableNotification(_ enable: Bool) async throws
```

```objc
- (void) enableNotification:(BOOL) enable completionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

HomeKit delivers notifications to the accessory delegate using the [`accessory(_:service:didUpdateValueFor:)`](../hmaccessorydelegate/accessory%28_,service,didupdatevaluefor%29.md) method.

## Parameters

- `enable`: [`true`](../../Swift/true.md) to enable notifications, [`false`](../../Swift/false.md) to disable notifications.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Receiving change notifications
- [var isNotificationEnabled: Bool](./isnotificationenabled.md)
  A Boolean indicating whether the characteristic has been set to send notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/enablenotification(_:completionhandler:))*