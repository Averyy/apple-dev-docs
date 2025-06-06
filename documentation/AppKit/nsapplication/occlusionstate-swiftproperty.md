# occlusionState

**Framework**: AppKit  
**Kind**: property

The occlusion state of the app.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var occlusionState: NSApplication.OcclusionState { get }
```

#### Discussion

The value of this property reflects whether any part of the app’s windows are visible to the user. Use this information to disable expensive screen updates when your app is not visible.

## See Also

- [class let didChangeOcclusionStateNotification: NSNotification.Name](nsapplication/didchangeocclusionstatenotification.md)
  Posted when the app’s occlusion state changes.
- [NSApplication.OcclusionState](nsapplication/occlusionstate-swift.struct.md)
  This constant indicates whether at least part of any window owned by this app is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/occlusionstate-swift.property)*