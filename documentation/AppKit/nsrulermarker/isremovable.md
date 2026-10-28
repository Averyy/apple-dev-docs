# isRemovable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the user can remove the receiver from its ruler view.

**Availability**:
- macOS

## Declaration

```swift
var isRemovable: Bool { get set }
```

```objc
@property (getter=isRemovable) BOOL removable;
```

## Discussion

[`true`](../../Swift/true.md) to allow the user to drag the marker image off of the ruler and remove the marker, [`false`](../../Swift/false.md) to prevent the user from removing the marker.

By default ruler markers are not removable.

## See Also

### Setting movability
- [var isMovable: Bool](./ismovable.md)
  A Boolean that indicates whether the user can move the receiver in its ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/isremovable)*