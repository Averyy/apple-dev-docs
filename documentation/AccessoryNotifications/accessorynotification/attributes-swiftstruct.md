# AccessoryNotification.Attributes

**Framework**: Accessory Notifications  
**Kind**: struct

Attributes that display priority for a notification.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
struct Attributes
```

#### Overview

Use these attributes to change the visual appearance of and add information about your notification. For guidance on whether to alert for a notification, see [`AlertingContext`](alertingcontext.md).

## Topics

### Identifying attribute types
- [static let critical: AccessoryNotification.Attributes](accessorynotification/attributes-swift.struct/critical.md)
  An attribute that indicates a critical notification.
- [static let priority: AccessoryNotification.Attributes](accessorynotification/attributes-swift.struct/priority.md)
  An attribute that indicates a priority notification.
- [static let timeSensitive: AccessoryNotification.Attributes](accessorynotification/attributes-swift.struct/timesensitive.md)
  An attribute that indicates a time-sensitive notification.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [let attributes: AccessoryNotification.Attributes](accessorynotification/attributes-swift.property.md)
  A set of attributes that indicate the notification’s priority level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/attributes-swift.struct)*