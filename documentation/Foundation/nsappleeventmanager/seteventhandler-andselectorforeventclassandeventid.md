# setEventHandler(_:andSelector:forEventClass:andEventID:)

**Framework**: Foundation  
**Kind**: method

Registers the Apple event handler specified by `handler` for the event specified by `eventClass` and `eventID`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setEventHandler(_ handler: Any, andSelector handleEventSelector: Selector, forEventClass eventClass: AEEventClass, andEventID eventID: AEEventID)
```

#### Discussion

If an event handler is already registered for the specified event class and event ID, removes it. The signature for `handler` should match the following:

```objc
- (void)handleAppleEvent:(NSAppleEventDescriptor *)event withReplyEvent: (NSAppleEventDescriptor *)replyEvent;
```

## See Also

- [func removeEventHandler(forEventClass: AEEventClass, andEventID: AEEventID)](nsappleeventmanager/removeeventhandler(foreventclass:andeventid:).md)
  If an Apple event handler has been registered for the event specified by `eventClass` and `eventID`, removes it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager/seteventhandler(_:andselector:foreventclass:andeventid:))*