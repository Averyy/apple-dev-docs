# coachingOverlayViewDidRequestSessionReset(_:)

**Framework**: ARKit  
**Kind**: method

Tells you when the user taps the coaching overlay view’s Start Over button while the session is relocalizing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func coachingOverlayViewDidRequestSessionReset(_ coachingOverlayView: ARCoachingOverlayView)
```

#### Discussion

Implement this function to do the actions your app requires to restart the AR experience. For example, you might hide custom relocalization UI, deallocate resources, or restore virtual content to a starting location.

If you don’t implement this function, the coaching overlay resets the session for you––equivalent to calling [`run(_:options:)`](arsession/run(_:options:).md) with the [`resetTracking`](arsession/runoptions/resettracking.md) option––when the user taps Start Over.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayviewdelegate/coachingoverlayviewdidrequestsessionreset(_:))*