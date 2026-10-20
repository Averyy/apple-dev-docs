# NSHapticFeedbackManager

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that provides access to the haptic feedback management attributes on a system with a Force Touch trackpad.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class NSHapticFeedbackManager
```

```objc
@interface NSHapticFeedbackManager : NSObject
```

## Topics

### Accessing the Default Feedback Performer
- [class var defaultPerformer: any NSHapticFeedbackPerformer](./nshapticfeedbackmanager/defaultperformer.md)
  Requests a haptic feedback performer object that is based on the current input device, accessibility settings, and user preferences.
### Enumerations
- [NSHapticFeedbackManager.FeedbackPattern](./nshapticfeedbackmanager/feedbackpattern.md)
  A pattern of haptic feedback to be provided to the user.
- [NSHapticFeedbackManager.PerformanceTime](./nshapticfeedbackmanager/performancetime.md)
  A time at which to provide haptic feedback to the user.

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

## See Also

### Trackpad
- [class NSPressureConfiguration](./nspressureconfiguration.md)
  An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshapticfeedbackmanager)*