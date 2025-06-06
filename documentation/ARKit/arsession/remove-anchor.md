# remove(anchor:)

**Framework**: ARKit  
**Kind**: method

Removes the specified anchor from tracking by the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func remove(anchor: ARAnchor)
```

#### Discussion

Changes to anchor tracking take effect when the next frame is captured.

## Parameters

- `anchor`: The anchor to remove.

## See Also

- [func add(anchor: ARAnchor)](arsession/add(anchor:).md)
  Adds the specified anchor to be tracked by the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/remove(anchor:))*