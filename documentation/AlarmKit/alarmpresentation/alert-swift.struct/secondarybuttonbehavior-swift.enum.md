# AlarmPresentation.Alert.SecondaryButtonBehavior

**Framework**: AlarmKit  
**Kind**: enum  
**Role**: Enumeration

Describes the behaviour of the second button.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum SecondaryButtonBehavior
```

#### Overview

You define your secondary action using `SecondaryButtonBehavior` parameter when creating alerting state of your alarm attributes. The secondary button is optional, you can choose to exclude it. The secondary button displays if you use `custom`.

## Topics

### Enumeration Cases
- [AlarmPresentation.Alert.SecondaryButtonBehavior.countdown](./secondarybuttonbehavior-swift.enum/countdown.md)
  A case that indicates the secondary button is a countdown.
- [AlarmPresentation.Alert.SecondaryButtonBehavior.custom](./secondarybuttonbehavior-swift.enum/custom.md)
  A case that indicates the secondary button has a custom behavior.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating a second button
- [var secondaryButton: AlarmButton?](./secondarybutton.md)
  The appearance of the secondary button.
- [var secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior?](./secondarybuttonbehavior-swift.property.md)
  The defined behavior of the second button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.enum)*