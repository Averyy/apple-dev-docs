# event

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The event which caused the anchor to update.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
let event: AnchorUpdate<AnchorType>.Event
```

## See Also

### Inspecting anchor updates
- [let anchor: AnchorType](./anchor.md)
  The anchor that this anchor update contains information about.
- [var timestamp: TimeInterval](./timestamp.md)
  The time when this anchor update occurred.
- [AnchorUpdate.Event](./event-swift.enum.md)
  An event that indicates whether an anchor was added, updated, or removed.
- [var description: String](./description.md)
  A textual representation of this anchor update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdate/event-swift.property)*