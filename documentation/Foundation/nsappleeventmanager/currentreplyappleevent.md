# currentReplyAppleEvent

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var currentReplyAppleEvent: NSAppleEventDescriptor? { get }
```

```objc
@property (retain, readonly, nullable) NSAppleEventDescriptor * currentReplyAppleEvent;
```

#### Discussion

An Apple event is being handled on the current thread if [`currentAppleEvent`](./currentappleevent.md) does not return `nil`. Returns `nil` otherwise. This descriptor, including any mutations, will be returned to the sender of the current event when all handling of the event has been completed, if the sender has requested a reply. The effects of retaining the descriptor are undefined; it may be copied, but mutations of the copy are not returned to the sender of the current event.

## See Also

### Suspending and resuming Apple events
- [func appleEvent(forSuspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor](./appleevent%28forsuspensionid%29.md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](./suspendcurrentappleevent%28%29.md), returns the descriptor for the event whose handling was suspended.
- [var currentAppleEvent: NSAppleEventDescriptor?](./currentappleevent.md)
  Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager/currentreplyappleevent)*