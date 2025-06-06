# applicationDidChangeOcclusionState(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate about changes to the app’s occlusion state.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
optional func applicationDidChangeOcclusionState(_ notification: Notification)
```

#### Discussion

Upon receiving this method, you can query the application for its occlusion state. Note that this only notifies about changes in the state of the occlusion, not when the occlusion region changes. You can use this method to increase responsiveness and save power by halting any expensive calculations that the user can not see.

## Parameters

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidchangeocclusionstate(_:))*