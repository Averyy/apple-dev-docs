# AlarmMetadata

**Framework**: AlarmKit  
**Kind**: protocol  
**Role**: Protocol

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
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Views
- [struct AlarmPresentation](./alarmpresentation.md)
  An object that describes the content required for the alarm UI.
- [struct AlarmPresentationState](./alarmpresentationstate.md)
  The system managed content state of an alarm Live Activity.
- [struct AlarmAttributes](./alarmattributes.md)
  An object that contains all information necessary for the alarm UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmetadata)*