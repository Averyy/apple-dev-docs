# AlarmPresentation.Alert.SecondaryButtonBehavior

**Framework**: AlarmKit  
**Kind**: enum

Describes the behaviour of the second button.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum SecondaryButtonBehavior
```

#### Overview

You define your secondary action using `SecondaryButtonBehavior` parameter when creating alerting state of your alarm attributes. The secondary button is optional, you can choose to exclude it. The secondary button displays if you use `custom`.

## Topics

### Enumeration Cases
- [AlarmPresentation.Alert.SecondaryButtonBehavior.countdown](alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.enum/countdown.md)
  A case that indicates the secondary button is a countdown.
- [AlarmPresentation.Alert.SecondaryButtonBehavior.custom](alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.enum/custom.md)
  A case that indicates the secondary button has a custom behavior.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var secondaryButton: AlarmButton?](alarmpresentation/alert-swift.struct/secondarybutton.md)
  The appearance of the secondary button.
- [var secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior?](alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.property.md)
  The behavior of the second button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.enum)*