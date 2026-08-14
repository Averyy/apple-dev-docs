# AlarmMetadata

**Framework**: AlarmKit  
**Kind**: protocol

A metadata object that contains information about an alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
protocol AlarmMetadata : Decodable, Encodable, Hashable, Sendable
```

#### Overview

Provide an implementation of this for your own custom content or other information. The implementation can be empty if you don’t want to provide any additional data for your alarm UI.

## Relationships

### Inherits From
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AlarmPresentation](alarmpresentation.md)
  An object that describes the content required for the alarm UI.
- [struct AlarmPresentationState](alarmpresentationstate.md)
  The system managed content state of an alarm Live Activity.
- [struct AlarmAttributes](alarmattributes.md)
  An object that contains all information necessary for the alarm UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmetadata)*