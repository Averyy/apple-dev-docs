# setEventHandler(_:andSelector:forEventClass:andEventID:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers the Apple event handler specified by `handler` for the event specified by `eventClass` and `eventID`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setEventHandler(_ handler: Any, andSelector handleEventSelector: Selector, forEventClass eventClass: AEEventClass, andEventID eventID: AEEventID)
```

```objc
- (void) setEventHandler:(id) handler andSelector:(SEL) handleEventSelector forEventClass:(AEEventClass) eventClass andEventID:(AEEventID) eventID;
```

#### Discussion

If an event handler is already registered for the specified event class and event ID, removes it. The signature for `handler` should match the following:

```objc
- (void)handleAppleEvent:(NSAppleEventDescriptor *)event withReplyEvent: (NSAppleEventDescriptor *)replyEvent;
```

## See Also

### Working with event handlers
- [func removeEventHandler(forEventClass: AEEventClass, andEventID: AEEventID)](./removeeventhandler%28foreventclass,andeventid%29.md)
  If an Apple event handler has been registered for the event specified by `eventClass` and `eventID`, removes it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager/seteventhandler(_:andselector:foreventclass:andeventid:))*