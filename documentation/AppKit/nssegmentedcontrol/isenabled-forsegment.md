# isEnabled(forSegment:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value indicating whether the specified segment is enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func isEnabled(forSegment segment: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the segment is enabled; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `segment`: The index of the segment whose enabled state you want to get. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func setEnabled(Bool, forSegment: Int)](nssegmentedcontrol/setenabled(_:forsegment:).md)
  Sets the enabled state of the specified segment


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/isenabled(forsegment:))*