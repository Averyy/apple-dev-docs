# AlarmAttributes

**Framework**: AlarmKit  
**Kind**: struct

An object that contains all information necessary for the alarm UI.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct AlarmAttributes<Metadata> where Metadata : AlarmMetadata
```

#### Overview

Provide all the information for the alarm up-front. At widget archiving time, the widget extension can choose which state to provide based on the mode in the [`AlarmPresentationState`](alarmpresentationstate.md) activity content state payload. The following example defines the attributes for the alarm UI.

```swift
let attributes = AlarmAttributes(presentation: presentation,
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
- [ActivityAttributes](../ActivityKit/ActivityAttributes.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AlarmPresentation](alarmpresentation.md)
  An object that describes the content required for the alarm UI.
- [struct AlarmPresentationState](alarmpresentationstate.md)
  An object that describes the mutable content of the alarm.
- [protocol AlarmMetadata](alarmmetadata.md)
  A metadata object that contains information about an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmattributes)*