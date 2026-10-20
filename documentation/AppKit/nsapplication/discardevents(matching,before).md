# discardEvents(matching:before:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes all events matching the given mask and generated before the specified event.

**Availability**:
- macOS

## Declaration

```swift
func discardEvents(matching mask: NSEvent.EventTypeMask, before lastEvent: NSEvent?)
```

```objc
- (void) discardEventsMatchingMask:(NSEventMask) mask beforeEvent:(NSEvent *) lastEvent;
```

#### Discussion

Use this method to ignore any events that occurred before a specific event. For example, suppose your app has a tracking loop that you exit when the user releases the mouse button. You could use this method, specifying `NSAnyEventMask` as the mask argument and the ending mouse-up event as the `lastEvent` argument, to discard all events that occurred while you were tracking mouse movements in your loop. Passing the mouse-up event as `lastEvent` ensures that any events that might have occurred after the mouse-up event (that is, that appear in the queue after the mouse-up event) aren’t discarded.

> **Note**:  Typically, you send this message to an [`NSWindow`](../nswindow.md) object, rather than to the app object. Discarding events for a window clears out all of the events for that window only, leaving events for other windows in place.

For the `mask` parameter, you can add together event type constants such as the following:

- `NSLeftMouseDownMask`
- `NSLeftMouseUpMask`
- `NSRightMouseDownMask`
- `NSRightMouseUpMask`
- `NSMouseMovedMask`
- `NSLeftMouseDraggedMask`
- `NSRightMouseDraggedMask`
- `NSMouseEnteredMask`
- `NSMouseExitedMask`
- `NSKeyDownMask`
- `NSKeyUpMask`
- `NSFlagsChangedMask`
- `NSPeriodicMask`
- `NSCursorUpdateMask`
- `NSAnyEventMask`

This method can also be called in subthreads. Events posted in subthreads bubble up in the main thread event queue.

## Parameters

- `mask`: Contains one or more flags indicating the types of events to discard. The constants section of the [`NSEvent`](../nsevent.md) class defines the constants you can add together to create this mask. The discussion section also lists some of the constants that are typically used.
- `lastEvent`: A marker event that you use to indicate which events should be discarded. Events that occurred before this event are discarded but those that occurred after it are not.

## See Also

### Managing the event loop
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](./nextevent%28matching,until,inmode,dequeue%29.md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [var currentEvent: NSEvent?](./currentevent.md)
  The last event object that the app retrieved from the event queue.
- [var isRunning: Bool](./isrunning.md)
  A Boolean value indicating whether the main event loop is running.
- [func run()](./run%28%29.md)
  Starts the main event loop.
- [func finishLaunching()](./finishlaunching%28%29.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [func stop(Any?)](./stop%28_%29.md)
  Stops the main event loop.
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  Dispatches an event to other objects.
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Adds a given event to the receiver’s event queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/discardevents(matching:before:))*