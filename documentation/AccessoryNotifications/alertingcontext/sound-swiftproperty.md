# sound

**Framework**: Accessory Notifications  
**Kind**: property

An optional sound configuration for the notification.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
var sound: AlertingContext.Sound? { get }
```

#### Discussion

A value of `nil` indicates the notification has no sound. Use the [`AlertingContext.Sound`](alertingcontext/sound-swift.struct.md) properties to determine sound characteristics.

## See Also

- [AlertingContext.Sound](alertingcontext/sound-swift.struct.md)
  A structure that describes sound characteristics for a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/sound-swift.property)*