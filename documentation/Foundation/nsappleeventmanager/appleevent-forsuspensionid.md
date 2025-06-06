# appleEvent(forSuspensionID:)

**Framework**: Foundation  
**Kind**: method

Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](nsappleeventmanager/suspendcurrentappleevent().md), returns the descriptor for the event whose handling was suspended.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func appleEvent(forSuspensionID suspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor
```

#### Discussion

The effects of mutating or retaining the returned descriptor are undefined, although it may be copied. [`appleEvent(forSuspensionID:)`](nsappleeventmanager/appleevent(forsuspensionid:).md) may be invoked in any thread, not just the one in which the corresponding invocation of [`suspendCurrentAppleEvent()`](nsappleeventmanager/suspendcurrentappleevent().md) occurred.

## See Also

- [var currentAppleEvent: NSAppleEventDescriptor?](nsappleeventmanager/currentappleevent.md)
  Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.
- [var currentReplyAppleEvent: NSAppleEventDescriptor?](nsappleeventmanager/currentreplyappleevent.md)
  Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.
- [func replyAppleEvent(forSuspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor](nsappleeventmanager/replyappleevent(forsuspensionid:).md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](nsappleeventmanager/suspendcurrentappleevent().md), returns the corresponding reply event descriptor.
- [func resume(withSuspensionID: NSAppleEventManager.SuspensionID)](nsappleeventmanager/resume(withsuspensionid:).md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](nsappleeventmanager/suspendcurrentappleevent().md), signal that handling of the suspended event may now continue.
- [func setCurrentAppleEventAndReplyEventWithSuspensionID(NSAppleEventManager.SuspensionID)](nsappleeventmanager/setcurrentappleeventandreplyeventwithsuspensionid(_:).md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](nsappleeventmanager/suspendcurrentappleevent().md), sets the values that will be returned by subsequent invocations of [`currentAppleEvent`](nsappleeventmanager/currentappleevent.md) and [`currentReplyAppleEvent`](nsappleeventmanager/currentreplyappleevent.md) to be the event whose handling was suspended and its corresponding reply event, respectively.
- [func suspendCurrentAppleEvent() -> NSAppleEventManager.SuspensionID?](nsappleeventmanager/suspendcurrentappleevent.md)
  Suspends the handling of the current event and returns an ID that must be used to resume the handling of the event if an Apple event is being handled on the current thread.
- [NSAppleEventManager.SuspensionID](nsappleeventmanager/suspensionid.md)
  Identifies an Apple event whose handling has been suspended. Can be used to resume handling of the Apple event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager/appleevent(forsuspensionid:))*