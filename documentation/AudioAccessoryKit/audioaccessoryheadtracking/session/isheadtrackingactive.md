# isHeadTrackingActive

**Framework**: AudioAccessoryKit  
**Kind**: property

Returns `true` when head tracking is currently enabled for this accessory; `false` otherwise.

**Availability**:
- iOS 27.0+ (Beta)

## Declaration

```swift
final var isHeadTrackingActive: Bool { get }
```

#### Discussion

Use this to bootstrap state at session start. After activation, prefer `headTrackingStateDidChange(isActive:)` for updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/session/isheadtrackingactive)*