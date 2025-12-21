# isRemovable

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the user can remove the receiver from its ruler view.

**Availability**:
- macOS ?+

## Declaration

```swift
var isRemovable: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) to allow the user to drag the marker image off of the ruler and remove the marker, [`false`](https://developer.apple.com/documentation/Swift/false) to prevent the user from removing the marker.

By default ruler markers are not removable.

## See Also

- [var isMovable: Bool](nsrulermarker/ismovable.md)
  A Boolean that indicates whether the user can move the receiver in its ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/isremovable)*