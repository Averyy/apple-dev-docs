# inputEventMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Retrieves the event types the filter accepts.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class var inputEventMask: NSEvent.EventTypeMask { get }
```

```objc
@property (class, readonly) NSEventMask inputEventMask;
```

#### Discussion

This method retrieves the event types that the filter accepts. This information may be used by an event tracking loop to watch for events that can be passed to the filter.

## See Also

### Related Documentation
- [class NSEvent](../nsevent.md)
  An object that contains information about an input action, such as a mouse click or a key press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/inputeventmask)*