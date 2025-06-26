# userActivity(_:element:_:)

**Framework**: FamilyControls  
**Kind**: method

Advertises a user activity type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
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

- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](familyactivitypicker/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](familyactivitypicker/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/useractivity(_:element:_:))*