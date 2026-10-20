# userActivity(_:isActive:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
func userActivity(_ activityType: String, isActive: Bool = true, _ update: @escaping (NSUserActivity) -> ()) -> some View
```

#### Discussion

You can use `userActivity(_:isActive:_:)` to start, stop, or modify the advertisement of a specific type of user activity.

The scope of the activity applies only to the scene or window the view is in.

## Parameters

- `activityType`: The type of activity to advertise.
- `isActive`: When `false`, avoids advertising the activity. Defaults to `true`.
- `update`: A function that modifies the passed-in activity for advertisement.

## See Also

### Sending and receiving user activities
- [Restoring your app’s state with SwiftUI](../restoring-your-app-s-state-with-swiftui.md)
  Provide app continuity for users by preserving their current activities.
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](./useractivity%28_,element,_%29.md)
  Advertises a user activity type.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](./oncontinueuseractivity%28_,perform%29.md)
  Registers a handler to invoke in response to a user activity that your app receives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/useractivity(_:isactive:_:))*