# createNewActivity()

**Framework**: ClassKit  
**Kind**: method

Creates and returns a new activity instance for the context.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func createNewActivity() -> CLSActivity
```

## Mentions

- [Recording student progress](recording-student-progress.md)

#### Return Value

A new activity.

#### Discussion

Use this method to create a new activity for a context every time the user makes a new attempt at a task. Afterward, you can use the returned value, or retrieve it by accessing the context’s [`currentActivity`](clscontext/currentactivity.md) property. However, don’t store a reference to the activity as a class property, because the underlying object may change from time to time as the framework performs network synchronization.

When you call this method on a context that already has an activity, the old activity is stopped and ceases to be accessible to your app, although its data remains in the network.

## See Also

- [var currentActivity: CLSActivity?](clscontext/currentactivity.md)
  The activity available for recording progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/createnewactivity())*