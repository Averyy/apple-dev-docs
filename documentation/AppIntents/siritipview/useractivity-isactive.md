# userActivity(_:isActive:_:)

**Framework**: App Intents  
**Kind**: method

Advertises a user activity type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
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
- `isActive`: When  , avoids advertising the activity. Defaults   to  .
- `update`: A function that modifies the passed-in activity for   advertisement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/useractivity(_:isactive:_:))*