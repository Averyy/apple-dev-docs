# userActivity(_:element:_:)

**Framework**: SwiftUI  
**Kind**: method

Advertises a user activity type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func userActivity<P>(_ activityType: String, element: P?, _ update: @escaping (P, NSUserActivity) -> ()) -> some View
```

#### Discussion

The scope of the activity applies only to the scene or window the view is in.

## Parameters

- `activityType`: The type of activity to advertise.
- `element`: If the element is  , the handler will not be   associated with the activity (and if there are no handlers, no   activity is advertised). The method passes the non-  element to   the handler as a convenience so the handlers don’t all need to   implement an early exit with   .
- `update`: A function that modifies the passed-in activity for   advertisement.

## See Also

- [Restoring Your App’s State with SwiftUI](restoring_your_app_s_state_with_swiftui.md)
  Provide app continuity for users by preserving their current activities.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](view/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](view/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/useractivity(_:element:_:))*