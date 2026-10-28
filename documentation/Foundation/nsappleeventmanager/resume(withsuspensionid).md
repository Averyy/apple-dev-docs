# resume(withSuspensionID:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md), signal that handling of the suspended event may now continue.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func resume(withSuspensionID suspensionID: NSAppleEventManager.SuspensionID)
```

```objc
- (void) resumeWithSuspensionID:(NSAppleEventManagerSuspensionID) suspensionID;
```

## Discussion

This may result in the immediate sending of the reply event to the sender of the suspended event, if the sender has requested a reply. If `suspensionID` has been used in a previous invocation of [`setCurrentAppleEventAndReplyEventWithSuspensionID(_:)`](./setcurrentappleeventandreplyeventwithsuspensionid%28_%29.md) the effects of that invocation are completely undone. Redundant invocations of [`resume(withSuspensionID:)`](./resume%28withsuspensionid%29.md) are ignored. Subsequent invocations of other `NSAppleEventManager` methods using the same suspension ID are invalid. [`resume(withSuspensionID:)`](./resume%28withsuspensionid%29.md) may be invoked in any thread, not just the one in which the corresponding invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md) occurred.

## See Also

### Suspending and resuming Apple events
- [func appleEvent(forSuspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor](./appleevent%28forsuspensionid%29.md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md), returns the descriptor for the event whose handling was suspended.
- [var currentAppleEvent: NSAppleEventDescriptor?](./currentappleevent.md)
  Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.
- [var currentReplyAppleEvent: NSAppleEventDescriptor?](./currentreplyappleevent.md)
  Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.
- [func replyAppleEvent(forSuspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor](./replyappleevent%28forsuspensionid%29.md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md), returns the corresponding reply event descriptor.
- [func setCurrentAppleEventAndReplyEventWithSuspensionID(NSAppleEventManager.SuspensionID)](./setcurrentappleeventandreplyeventwithsuspensionid%28_%29.md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md), sets the values that will be returned by subsequent invocations of [`currentAppleEvent`](./currentappleevent.md) and [`currentReplyAppleEvent`](./currentreplyappleevent.md) to be the event whose handling was suspended and its corresponding reply event, respectively.
- [func suspendCurrentAppleEvent() -> NSAppleEventManager.SuspensionID?](./suspendcurrentappleevent%28%29.md)
  Suspends the handling of the current event and returns an ID that must be used to resume the handling of the event if an Apple event is being handled on the current thread.
- [NSAppleEventManager.SuspensionID](./suspensionid.md)
  Identifies an Apple event whose handling has been suspended. Can be used to resume handling of the Apple event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager/resume(withsuspensionid:))*