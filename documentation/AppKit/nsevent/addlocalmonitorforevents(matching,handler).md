# addLocalMonitorForEvents(matching:handler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Installs an event monitor that receives copies of events the system posts to this app prior to their dispatch.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func addLocalMonitorForEvents(matching mask: NSEvent.EventTypeMask, handler block: @escaping (NSEvent) -> NSEvent?) -> Any?
```

```objc
+ (id) addLocalMonitorForEventsMatchingMask:(NSEventMask) mask handler:(NSEvent * (^)(NSEvent *event)) block;
```

#### Return Value

An event handler object.

#### Discussion

Your handler will not be called for events that are consumed by nested event-tracking loops such as control tracking, menu tracking, or window dragging; only events that are dispatched through the applications [`sendEvent(_:)`](../nsapplication/sendevent%28_%29.md) method will be passed to your handler.

> **Note**:  The monitor Block is called for all future events that match `mask`. You must call [`removeMonitor(_:)`](./removemonitor%28_%29.md) to stop the monitor.

##### Special Considerations

In OS X v 10.6, event monitors are only able to monitor the following event types:

- [`NSFlagsChanged`](../nsflagschanged.md)
- [`NSLeftMouseDragged`](../nsleftmousedragged.md)
- [`NSRightMouseDragged`](../nsrightmousedragged.md)
- [`NSOtherMouseDragged`](../nsothermousedragged.md)
- [`NSLeftMouseUp`](../nsleftmouseup.md)
- [`NSRightMouseUp`](../nsrightmouseup.md)
- [`NSOtherMouseUp`](../nsothermouseup.md)
- [`NSLeftMouseDown`](../nsleftmousedown.md)
- [`NSRightMouseDown`](../nsrightmousedown.md)
- [`NSOtherMouseDown`](../nsothermousedown.md)
- [`NSMouseMoved`](../nsmousemoved.md)
- [`NSFlagsChanged`](../nsflagschanged.md)
- [`NSScrollWheel`](../nsscrollwheel.md)
- [`NSTabletPoint`](../nstabletpoint.md)
- [`NSTabletProximity`](../nstabletproximity.md)
- [`NSKeyDown`](../nskeydown.md) (Key repeats are determined using the [`isARepeat`](./isarepeat.md) property.)

## Parameters

- `mask`: An event mask specifying which events you wish to monitor. See [`NSEvent.EventTypeMask`](./eventtypemask.md) for possible values.
- `block`: The event handler block object. It is passed the event to monitor. You can return the event unmodified, create and return a new NSEvent object, or return nil to stop the dispatching of the event.

## See Also

### Monitoring app events
- [class func addGlobalMonitorForEvents(matching: NSEvent.EventTypeMask, handler: (NSEvent) -> Void) -> Any?](./addglobalmonitorforevents%28matching,handler%29.md)
  Installs an event monitor that receives copies of events the system posts to other applications.
- [class func removeMonitor(Any)](./removemonitor%28_%29.md)
  Removes the specified event monitor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/addlocalmonitorforevents(matching:handler:))*