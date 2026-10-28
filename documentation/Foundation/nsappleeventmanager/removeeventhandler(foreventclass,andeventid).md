# removeEventHandler(forEventClass:andEventID:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

If an Apple event handler has been registered for the event specified by `eventClass` and `eventID`, removes it.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func removeEventHandler(forEventClass eventClass: AEEventClass, andEventID eventID: AEEventID)
```

```objc
- (void) removeEventHandlerForEventClass:(AEEventClass) eventClass andEventID:(AEEventID) eventID;
```

## Discussion

Otherwise does nothing.

## See Also

### Working with event handlers
- [func setEventHandler(Any, andSelector: Selector, forEventClass: AEEventClass, andEventID: AEEventID)](./seteventhandler%28_,andselector,foreventclass,andeventid%29.md)
  Registers the Apple event handler specified by `handler` for the event specified by `eventClass` and `eventID`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager/removeeventhandler(foreventclass:andeventid:))*