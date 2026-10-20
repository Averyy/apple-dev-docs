# SRTextInputSession

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

The characters a user types for a particular keyboard.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class SRTextInputSession
```

```objc
@interface SRTextInputSession : NSObject
```

#### Overview

The framework instantiates a new instance of this class every time the keyboard displays after dismissal.

## Topics

### Identifying the Session
- [var sessionIdentifier: String](./srtextinputsession/sessionidentifier.md)
  A unique identifier for the keyboard session.
### Timing Text Input
- [var duration: TimeInterval](./srtextinputsession/duration.md)
  The length of time, in seconds, that the session spans.
### Inspecting Text Source
- [var sessionType: SRTextInputSession.SessionType](./srtextinputsession/sessiontype-swift.property.md)
- [SRTextInputSession.SessionType](./srtextinputsession/sessiontype-swift.enum.md)
  Methods to input text during a session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting Text Input
- [var textInputSessions: [SRTextInputSession]](./srdeviceusagereport/applicationusage/textinputsessions.md)
  The text input session types that occur during application usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srtextinputsession)*