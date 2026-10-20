# add(anchor:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified anchor to be tracked by the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
func add(anchor: ARAnchor)
```

```objc
- (void) addAnchor:(ARAnchor *) anchor;
```

#### Discussion

Changes to anchor tracking take effect when the next frame is captured.

## Parameters

- `anchor`: The anchor to add.

## See Also

### Managing anchors
- [func remove(anchor: ARAnchor)](./remove%28anchor%29.md)
  Removes the specified anchor from tracking by the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/add(anchor:))*