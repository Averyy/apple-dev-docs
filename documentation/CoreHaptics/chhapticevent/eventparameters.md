# eventParameters

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

An array of event parameters, possibly empty.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var eventParameters: [CHHapticEventParameter] { get }
```

```objc
@property (readonly) NSArray<CHHapticEventParameter *> * eventParameters;
```

## See Also

### Configuring Haptic Events
- [CHHapticEvent.ParameterID](./parameterid.md)
  An identifier for an event parameter.
- [var relativeTime: TimeInterval](./relativetime.md)
  The start time of the event, relative to other events in the same pattern.
- [var duration: TimeInterval](./duration.md)
  The duration of the haptic event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventparameters)*