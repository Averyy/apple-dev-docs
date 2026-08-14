# AlarmAttributes

**Framework**: AlarmKit  
**Kind**: struct

An object that contains all information necessary for the alarm UI.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct AlarmAttributes<Metadata> where Metadata : AlarmMetadata
```

#### Overview

This struct includes alerting, countdown, and paused states. You define all the alarm information when creating the attributes. When archiving the widget, the widget extension selects which state to display based on the [`AlarmPresentationState`](alarmpresentationstate.md) provided in the activity content state payload. The following example defines the attributes for the alarm UI.

```swift
let attributes = AlarmAttributes(
    presentation: presentation,
    metadata: metadata,
    tintColor: Color.white)
```

## Topics

### Creating an alarm attribute
- [init(presentation: AlarmPresentation, metadata: Metadata?, tintColor: Color)](alarmattributes/init(presentation:metadata:tintcolor:).md)
  Creates an instance of an alarm UI.
- [var tintColor: Color](alarmattributes/tintcolor.md)
  The tint color applied to the templated UI.
- [var presentation: AlarmPresentation](alarmattributes/presentation.md)
  The content required for the various states of the UI.
- [var metadata: Metadata?](alarmattributes/metadata.md)
  The additional data you can include in your attributes.
- [AlarmAttributes.ContentState](alarmattributes/contentstate.md)
  The type alias for the structure that describes the content of an alarm.
### Decoding and encoding
- [init(from: any Decoder) throws](alarmattributes/init(from:).md)
  Creates an instance from the given decoder.
- [func encode(to: any Encoder) throws](alarmattributes/encode(to:).md)
  Performs encoding of the value using the given encoder.

## Relationships

### Conforms To
- [ActivityAttributes](../activitykit/activityattributes.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AlarmPresentation](alarmpresentation.md)
  An object that describes the content required for the alarm UI.
- [struct AlarmPresentationState](alarmpresentationstate.md)
  The system managed content state of an alarm Live Activity.
- [protocol AlarmMetadata](alarmmetadata.md)
  A metadata object that contains information about an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmattributes)*