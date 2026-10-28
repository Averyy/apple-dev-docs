# remove(anchor:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified anchor from tracking by the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
func remove(anchor: ARAnchor)
```

```objc
- (void) removeAnchor:(ARAnchor *) anchor;
```

## Discussion

Changes to anchor tracking take effect when the next frame is captured.

## Parameters

- `anchor`: The anchor to remove.

## See Also

### Managing anchors
- [func add(anchor: ARAnchor)](./add%28anchor%29.md)
  Adds the specified anchor to be tracked by the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/remove(anchor:))*