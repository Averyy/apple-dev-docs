# NSHapticFeedbackManager

**Framework**: AppKit  
**Kind**: class

An object that provides access to the haptic feedback management attributes on a system with a Force Touch trackpad.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class NSHapticFeedbackManager
```

## Topics

### Accessing the Default Feedback Performer
- [class var defaultPerformer: any NSHapticFeedbackPerformer](nshapticfeedbackmanager/defaultperformer.md)
  Requests a haptic feedback performer object that is based on the current input device, accessibility settings, and user preferences.
### Enumerations
- [NSHapticFeedbackManager.FeedbackPattern](nshapticfeedbackmanager/feedbackpattern.md)
  A pattern of haptic feedback to be provided to the user.
- [NSHapticFeedbackManager.PerformanceTime](nshapticfeedbackmanager/performancetime.md)
  A time at which to provide haptic feedback to the user.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class NSPressureConfiguration](nspressureconfiguration.md)
  An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshapticfeedbackmanager)*