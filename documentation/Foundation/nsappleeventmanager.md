# NSAppleEventManager

**Framework**: Foundation  
**Kind**: class

A mechanism for registering handler routines for specific types of Apple events and dispatching events to those handlers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSAppleEventManager
```

#### Overview

Cocoa provides built-in scriptability support that uses scriptability information supplied by an application to automatically convert Apple events into script command objects that perform the desired operation. However, some applications may want to perform more basic Apple event handling, in which an application registers handlers for the Apple events it can process, then calls on the Apple Event Manager to dispatch received Apple events to the appropriate handler. `NSAppleEventManager` supports these mechanisms by providing methods to register and remove handlers and to dispatch Apple events to the appropriate handler, if one exists. For related information, see [`How Cocoa Applications Handle Apple Events`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_handle_AEs/SAppsHandleAEs.html#//apple_ref/doc/uid/20001239)

Each application has at most one instance of `NSAppleEventManager`. To obtain a reference to it, you call the class method [`shared()`](nsappleeventmanager/shared().md), which creates the instance if it doesn’t already exist.

For information about the Apple Event Manager, see [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager) and Apple Events Programming Guide.

## Topics

### Getting an event manager
- [class func shared() -> NSAppleEventManager](nsappleeventmanager/shared.md)
  Returns the single instance of `NSAppleEventManager`, creating it first if it doesn’t exist.
### Working with event handlers
- [func removeEventHandler(forEventClass: AEEventClass, andEventID: AEEventID)](nsappleeventmanager/removeeventhandler(foreventclass:andeventid:).md)
  If an Apple event handler has been registered for the event specified by `eventClass` and `eventID`, removes it.
- [func setEventHandler(Any, andSelector: Selector, forEventClass: AEEventClass, andEventID: AEEventID)](nsappleeventmanager/seteventhandler(_:andselector:foreventclass:andeventid:).md)
  Registers the Apple event handler specified by `handler` for the event specified by `eventClass` and `eventID`.
### Working with events
- [func dispatchRawAppleEvent(UnsafePointer<AppleEvent>, withRawReply: UnsafeMutablePointer<AppleEvent>, handlerRefCon: SRefCon) -> OSErr](nsappleeventmanager/dispatchrawappleevent(_:withrawreply:handlerrefcon:).md)
  Causes the Apple event specified by `theAppleEvent` to be dispatched to the appropriate Apple event handler, if one has been registered by calling [`setEventHandler(_:andSelector:forEventClass:andEventID:)`](nsappleeventmanager/seteventhandler(_:andselector:foreventclass:andeventid:).md).
### Suspending and resuming Apple events
- [func appleEvent(forSuspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor](nsappleeventmanager/appleevent(forsuspensionid:).md)
  Given a nonzero `suspensionID` returned by an invocation of [`suspendCurrentAppleEvent()`](nsappleeventmanager/suspendcurrentappleevent().md), returns the descriptor for the event whose handling was suspended.
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
### Constants
- [NSAppleEvent Timeouts](nsappleevent-timeouts.md)
  The following constants should not be used and may eventually be removed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSAppleEventDescriptor](nsappleeventdescriptor.md)
  A wrapper for the Apple event descriptor data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager)*