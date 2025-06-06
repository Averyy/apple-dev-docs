# removeEventHandler(forEventClass:andEventID:)

**Framework**: Foundation  
**Kind**: method

If an Apple event handler has been registered for the event specified by `eventClass` and `eventID`, removes it.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func removeEventHandler(forEventClass eventClass: AEEventClass, andEventID eventID: AEEventID)
```

#### Discussion

Otherwise does nothing.

## See Also

- [func setEventHandler(Any, andSelector: Selector, forEventClass: AEEventClass, andEventID: AEEventID)](nsappleeventmanager/seteventhandler(_:andselector:foreventclass:andeventid:).md)
  Registers the Apple event handler specified by `handler` for the event specified by `eventClass` and `eventID`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventmanager/removeeventhandler(foreventclass:andeventid:))*