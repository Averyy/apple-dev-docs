# AlarmMetadata

**Framework**: AlarmKit  
**Kind**: protocol

A metadata object that contains information about an alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol AlarmMetadata : Decodable, Encodable, Hashable, Sendable
```

#### Overview

Provide an implementation of this for your own custom content or other information. The implementation can be empty if you don’t want to provide any additional data for your alarm UI.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AlarmPresentation](alarmpresentation.md)
  An object that describes the content required for the alarm UI.
- [struct AlarmPresentationState](alarmpresentationstate.md)
  An object that describes the mutable content of the alarm.
- [struct AlarmAttributes](alarmattributes.md)
  An object that contains all information necessary for the alarm UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmetadata)*