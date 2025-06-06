# add(anchor:)

**Framework**: ARKit  
**Kind**: method

Adds the specified anchor to be tracked by the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func add(anchor: ARAnchor)
```

#### Discussion

Changes to anchor tracking take effect when the next frame is captured.

## Parameters

- `anchor`: The anchor to add.

## See Also

- [func remove(anchor: ARAnchor)](arsession/remove(anchor:).md)
  Removes the specified anchor from tracking by the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/add(anchor:))*