# resolution

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The event’s resolution.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
var resolution: CMFallDetectionEvent.UserResolution { get }
```

```objc
@property (nonatomic, readonly) CMFallDetectionEventUserResolution resolution;
```

#### Discussion

The resolution of an event reflects the user’s action in response to the fall detection notification. For example, the user might tap a button to respond inside the notification, or press the digital crown to dismiss the notification.

## See Also

### Accessing Fall Data
- [CMFallDetectionEvent.UserResolution](./userresolution.md)
  User resolutions for fall detection events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/resolution)*