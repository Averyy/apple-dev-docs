# userActivity

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An object encapsulating a user activity supported by this responder.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var userActivity: NSUserActivity? { get set }
```

```objc
@property (strong, nullable) NSUserActivity * userActivity;
```

#### Discussion

By setting the [`userActivity`](./useractivity.md) property on a responder, the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object becomes managed by AppKit. You should override [`updateUserActivityState(_:)`](./updateuseractivitystate%28_%29.md) to write lazily any state data representing the user’s activity to the `userInfo` dictionary. AppKit automatically saves user activities it manages at appropriate times. Multiple responders can share a single [`NSUserActivity`](../../Foundation/nsuseractivity.md) instance, in which case they all get a callback, such as [`updateUserActivityState(_:)`](./updateuseractivitystate%28_%29.md), when the system updates the user activity object.

> **Note**:  Before the update callbacks are sent, the activity object’s `userInfo` dictionary is cleared.

In macOS, [`NSUserActivity`](../../Foundation/nsuseractivity.md) objects managed by [`NSResponder`](../nsresponder.md) automatically [`becomeCurrent()`](../../Foundation/nsuseractivity/becomecurrent%28%29.md) based on the main window and the responder chain.

A responder object can set its [`userActivity`](./useractivity.md) property to `nil` if it no longer wants to participate. Any [`NSUserActivity`](../../Foundation/nsuseractivity.md) objects that AppKit manages but have no associated responders (or documents) are automatically invalidated.

You can use this property from any thread, and it’s key-value observable (KVO).

## See Also

### Supporting User Activities
- [func updateUserActivityState(NSUserActivity)](./updateuseractivitystate%28_%29.md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/useractivity)*