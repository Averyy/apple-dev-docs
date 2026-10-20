# AccessoryNotification.Attributes

**Framework**: Accessory Notifications  
**Kind**: struct  
**Role**: Structure

Attributes that display priority for a notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct Attributes
```

#### Overview

Use these attributes to change the visual appearance of and add information about your notification. For guidance on whether to alert for a notification, see [`AlertingContext`](../alertingcontext.md).

## Topics

### Identifying attribute types
- [static let critical: AccessoryNotification.Attributes](./attributes-swift.struct/critical.md)
  An attribute that indicates a critical notification.
- [static let priority: AccessoryNotification.Attributes](./attributes-swift.struct/priority.md)
  An attribute that indicates a priority notification.
- [static let timeSensitive: AccessoryNotification.Attributes](./attributes-swift.struct/timesensitive.md)
  An attribute that indicates a time-sensitive notification.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Working with notification attributes
- [let attributes: AccessoryNotification.Attributes](./attributes-swift.property.md)
  A set of attributes that indicate the notification’s priority level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/attributes-swift.struct)*