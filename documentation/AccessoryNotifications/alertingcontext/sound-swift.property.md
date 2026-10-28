# sound

**Framework**: Accessory Notifications  
**Kind**: property  
**Role**: Instance Property

An optional sound configuration for the notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
var sound: AlertingContext.Sound? { get }
```

## Discussion

A value of `nil` indicates the notification has no sound. Use the [`AlertingContext.Sound`](./sound-swift.struct.md) properties to determine sound characteristics.

## See Also

### Configuring notification sound
- [AlertingContext.Sound](./sound-swift.struct.md)
  A structure that describes sound characteristics for a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/sound-swift.property)*