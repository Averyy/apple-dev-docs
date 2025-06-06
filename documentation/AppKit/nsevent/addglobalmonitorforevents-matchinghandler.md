# addGlobalMonitorForEvents(matching:handler:)

**Framework**: AppKit  
**Kind**: method

Installs an event monitor that receives copies of events the system posts to other applications.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func addGlobalMonitorForEvents(matching mask: NSEvent.EventTypeMask, handler block: @escaping (NSEvent) -> Void) -> Any?
```

#### Return Value

An event handler object.

#### Discussion

Events are delivered asynchronously to your app and you can only observe the event; you cannot modify or otherwise prevent the event from being delivered to its original target application.

Key-related events may only be monitored if accessibility is enabled or if your application is trusted for accessibility access (see [`AXIsProcessTrusted()`](https://developer.apple.com/documentation/applicationservices/1460720-axisprocesstrusted)).

Note that your handler will not be called for events that are sent to your own application.

##### Special Considerations

In OS X v 10.6, event monitors are only able to monitor the following event types:

- [`NSLeftMouseDragged`](nsleftmousedragged.md)
- [`NSRightMouseDragged`](nsrightmousedragged.md)
- [`NSOtherMouseDragged`](nsothermousedragged.md)
- [`NSLeftMouseUp`](nsleftmouseup.md)
- [`NSRightMouseUp`](nsrightmouseup.md)
- [`NSOtherMouseUp`](nsothermouseup.md)
- [`NSLeftMouseDown`](nsleftmousedown.md)
- [`NSRightMouseDown`](nsrightmousedown.md)
- [`NSOtherMouseDown`](nsothermousedown.md)
- [`NSMouseMoved`](nsmousemoved.md)
- [`NSFlagsChanged`](nsflagschanged.md)
- [`NSScrollWheel`](nsscrollwheel.md)
- [`NSTabletPoint`](nstabletpoint.md)
- [`NSTabletProximity`](nstabletproximity.md)
- [`NSKeyDown`](nskeydown.md) (Key repeats are determined using the [`isARepeat`](nsevent/isarepeat.md) property.)

## Parameters

- `mask`: An event mask specifying which events you wish to monitor. See   for possible values.
- `block`: The event handler block object. It is passed the event to monitor. You are unable to change the event, merely observe it.

## See Also

- [class func addLocalMonitorForEvents(matching: NSEvent.EventTypeMask, handler: (NSEvent) -> NSEvent?) -> Any?](nsevent/addlocalmonitorforevents(matching:handler:).md)
  Installs an event monitor that receives copies of events the system posts to this app prior to their dispatch.
- [class func removeMonitor(Any)](nsevent/removemonitor(_:).md)
  Removes the specified event monitor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/addglobalmonitorforevents(matching:handler:))*