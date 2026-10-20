# currentAppleEvent

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var currentAppleEvent: NSAppleEventDescriptor? { get }
```

```objc
@property (retain, readonly, nullable) NSAppleEventDescriptor * currentAppleEvent;
```

#### Discussion

An Apple event is being handled on the current thread if a handler that was registered with [`setEventHandler(_:andSelector:forEventClass:andEventID:)`](./seteventhandler%28_,andselector,foreventclass,andeventid%29.md) is being messaged at this instant or [`setCurrentAppleEventAndReplyEventWithSuspensionID(_:)`](./setcurrentappleeventandreplyeventwithsuspensionid%28_%29.md) has just been invoked. Returns `nil` otherwise. The effects of mutating or retaining the returned descriptor are undefined, although it may be copied.

## See Also

### Suspending and resuming Apple events
- [func appleEvent(forSuspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor](./appleevent%28forsuspensionid%29.md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md), returns the descriptor for the event whose handling was suspended.
- [var currentReplyAppleEvent: NSAppleEventDescriptor?](./currentreplyappleevent.md)
  Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.
- [func replyAppleEvent(forSuspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor](./replyappleevent%28forsuspensionid%29.md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md), returns the corresponding reply event descriptor.
- [func resume(withSuspensionID: NSAppleEventManager.SuspensionID)](./resume%28withsuspensionid%29.md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md), signal that handling of the suspended event may now continue.
- [func setCurrentAppleEventAndReplyEventWithSuspensionID(NSAppleEventManager.SuspensionID)](./setcurrentappleeventandreplyeventwithsuspensionid%28_%29.md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md), sets the values that will be returned by subsequent invocations of [`currentAppleEvent`](./currentappleevent.md) and [`currentReplyAppleEvent`](./currentreplyappleevent.md) to be the event whose handling was suspended and its corresponding reply event, respectively.
- [func suspendCurrentAppleEvent() -> NSAppleEventManager.SuspensionID?](./suspendcurrentappleevent%28%29.md)
  Suspends the handling of the current event and returns an ID that must be used to resume the handling of the event if an Apple event is being handled on the current thread.
- [NSAppleEventManager.SuspensionID](./suspensionid.md)
  Identifies an Apple event whose handling has been suspended. Can be used to resume handling of the Apple event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager/currentappleevent)*