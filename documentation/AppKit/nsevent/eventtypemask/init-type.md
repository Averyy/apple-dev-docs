# init(type:)

**Framework**: AppKit  
**Kind**: init

Returns the event mask for the specified type.

**Availability**:
- macOS ?+

## Declaration

```swift
init(type: NSEvent.EventType)
```

#### Return Value

The event mask corresponding to the specified type. The returned mask is equivalent to the number 1 left-shifted by `type` bits.

## Parameters

- `type`: The event type whose mask you want to get.

## See Also

- [NSEvent.EventTypeMask](nsevent/eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [NSEvent.ButtonMask](nsevent/buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct.md)
  Flags that represent key states in an event object.
- [NSEvent.Phase](nsevent/phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions.md)
  Constants that specify swipe-tracking options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/init(type:))*