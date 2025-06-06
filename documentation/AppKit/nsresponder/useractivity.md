# userActivity

**Framework**: Appkit  
**Kind**: property

An object encapsulating a user activity supported by this responder.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var userActivity: NSUserActivity? { get set }
```

#### Discussion

By setting the [`userActivity`](nsresponder/useractivity.md) property on a responder, the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object becomes managed by AppKit. You should override [`updateUserActivityState(_:)`](nsresponder/updateuseractivitystate(_:).md) to write lazily any state data representing the user’s activity to the `userInfo` dictionary. AppKit automatically saves user activities it manages at appropriate times. Multiple responders can share a single [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) instance, in which case they all get a callback, such as [`updateUserActivityState(_:)`](nsresponder/updateuseractivitystate(_:).md), when the system updates the user activity object.

> **Note**:  Before the update callbacks are sent, the activity object’s `userInfo` dictionary is cleared.

In macOS, [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects managed by [`NSResponder`](nsresponder.md) automatically [`becomeCurrent()`](https://developer.apple.com/documentation/foundation/nsuseractivity/1413665-becomecurrent) based on the main window and the responder chain.

A responder object can set its [`userActivity`](nsresponder/useractivity.md) property to `nil` if it no longer wants to participate. Any [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects that AppKit manages but have no associated responders (or documents) are automatically invalidated.

You can use this property from any thread, and it’s key-value observable (KVO).

## See Also

- [func updateUserActivityState(NSUserActivity)](nsresponder/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nsresponder/useractivity)*