# currentAppleEvent

**Framework**: Foundation  
**Kind**: property

Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var currentAppleEvent: NSAppleEventDescriptor? { get }
```

#### Discussion

An Apple event is being handled on the current thread if a handler that was registered with [`setEventHandler(_:andSelector:forEventClass:andEventID:)`](nsappleeventmanager/seteventhandler(_:andselector:foreventclass:andeventid:).md) is being messaged at this instant or [`setCurrentAppleEventAndReplyEventWithSuspensionID(_:)`](nsappleeventmanager/setcurrentappleeventandreplyeventwithsuspensionid(_:).md) has just been invoked. Returns `nil` otherwise. The effects of mutating or retaining the returned descriptor are undefined, although it may be copied.

## See Also

- [func appleEvent(forSuspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor](nsappleeventmanager/appleevent(forsuspensionid:).md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](nsappleeventmanager/suspendcurrentappleevent().md), returns the descriptor for the event whose handling was suspended.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager/currentappleevent)*