# presenceEventType

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The event type that triggers the presence event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var presenceEventType: HMPresenceEventType { get set }
```

```objc
@property (nonatomic, readwrite) HMPresenceEventType presenceEventType;
```

## Discussion

Use this property to change the presence type that triggers this event.

## See Also

### Configuring a presence event
- [var presenceUserType: HMPresenceEventUserType](./presenceusertype.md)
  The user type whose presence triggers the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablepresenceevent/presenceeventtype)*