# CMFallDetectionEvent.UserResolution.dismissed

**Framework**: Core Motion  
**Kind**: case  
**Role**: Case

The user dismissed the fall event alert, but didn’t explicitly confirm or reject the event.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
case dismissed
```

```c
CMFallDetectionEventUserResolutionDismissed
```

#### Discussion

The user can dismiss the alert by pressing the digital crown or tapping the close button.

## See Also

### Resolutions
- [CMFallDetectionEvent.UserResolution.confirmed](./confirmed.md)
  The user confirmed the event.
- [CMFallDetectionEvent.UserResolution.rejected](./rejected.md)
  The user rejected the fall event.
- [CMFallDetectionEvent.UserResolution.unresponsive](./unresponsive.md)
  The user didn’t respond to the fall event and the system hasn’t detected recovery motions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/dismissed)*