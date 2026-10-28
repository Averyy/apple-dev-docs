# isMovable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the user can move the receiver in its ruler view.

**Availability**:
- macOS

## Declaration

```swift
var isMovable: Bool { get set }
```

```objc
@property (getter=isMovable) BOOL movable;
```

## Discussion

[`true`](../../Swift/true.md) to allow the user to drag the marker image in the ruler, [`false`](../../Swift/false.md) to make it immobile.

By default, ruler markers are movable.

## See Also

### Setting movability
- [var isRemovable: Bool](./isremovable.md)
  A Boolean that indicates whether the user can remove the receiver from its ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/ismovable)*