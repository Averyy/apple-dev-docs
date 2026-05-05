# ForwardingDecision

**Framework**: Accessory Notifications  
**Kind**: enum

Possible decisions in response to the notification forwarding permission prompt.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
enum ForwardingDecision
```

#### Overview

When your app calls [`requestForwarding(for:)`](accessorynotificationcenter/requestforwarding(for:).md), the system prompts the person to choose which apps can forward notifications to your accessory.

## Topics

### Identifying the decision
- [ForwardingDecision.allow](forwardingdecision/allow.md)
  An option that indicates the person allows notifications from all applicable apps.
- [ForwardingDecision.deny](forwardingdecision/deny.md)
  An option that indicates the person doesn’t allow notification forwarding.
- [ForwardingDecision.limited](forwardingdecision/limited.md)
  An option that indicates the person allows notifications from a selected subset of apps.
- [ForwardingDecision.undetermined](forwardingdecision/undetermined.md)
  An option that indicates the person dismissed the prompt without responding.
### Accessing the decision’s description
- [var description: String](forwardingdecision/description.md)
  A textual representation of the decision.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class AccessoryNotificationCenter](accessorynotificationcenter.md)
  A class that enables an app to request permission for notification forwarding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/forwardingdecision)*