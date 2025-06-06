# CMFallDetectionEvent.UserResolution.dismissed

**Framework**: Core Motion  
**Kind**: case

The user dismissed the fall event alert, but didn’t explicitly confirm or reject the event.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
case dismissed
```

#### Discussion

The user can dismiss the alert by pressing the digital crown or tapping the close button.

## See Also

- [CMFallDetectionEvent.UserResolution.confirmed](cmfalldetectionevent/userresolution/confirmed.md)
  The user confirmed the event.
- [CMFallDetectionEvent.UserResolution.rejected](cmfalldetectionevent/userresolution/rejected.md)
  The user rejected the fall event.
- [CMFallDetectionEvent.UserResolution.unresponsive](cmfalldetectionevent/userresolution/unresponsive.md)
  The user didn’t respond to the fall event and the system hasn’t detected recovery motions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/dismissed)*