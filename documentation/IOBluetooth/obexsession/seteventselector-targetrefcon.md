# setEventSelector(_:target:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

Allow you to set a selector to be called when events occur on the OBEX session.

**Availability**:
- macOS ?+

## Declaration

```swift
func setEventSelector(_ inEventSelector: Selector!, target inEventSelectorTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!)
```

#### Discussion

Really not needed to be used, since the event selector will get set when an OBEX command is sent out.

## Parameters

- `inEventSelector`: Selector to call on the target.
- `inEventSelectorTarget`: Target to be called with the selector.
- `inUserRefCon`: User’s refCon that will get passed when their event callback is invoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/seteventselector(_:target:refcon:))*