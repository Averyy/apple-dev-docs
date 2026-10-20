# timestamp

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The time when this anchor update occurred.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

## See Also

### Inspecting anchor updates
- [let anchor: AnchorType](./anchor.md)
  The anchor that this anchor update contains information about.
- [let event: AnchorUpdate<AnchorType>.Event](./event-swift.property.md)
  The event which caused the anchor to update.
- [AnchorUpdate.Event](./event-swift.enum.md)
  An event that indicates whether an anchor was added, updated, or removed.
- [var description: String](./description.md)
  A textual representation of this anchor update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdate/timestamp)*