# setEventForwardingMask(_:)

**Framework**: Quartz  
**Kind**: method

Sets the mask used to filter which types of events are forwarded from the view to the composition during rendering.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setEventForwardingMask(_ mask: Int)
```

## Parameters

- `mask`: An event filtering mask. The mask can be a combination of any of the mask constants listed below, or the constant  .

## See Also

- [func eventForwardingMask() -> Int](qcview/eventforwardingmask.md)
  Retrieves the mask used to filter which types of events are forwarded from the view to the composition during rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/seteventforwardingmask(_:))*