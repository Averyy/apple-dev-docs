# init(anchor:)

**Framework**: ARKit  
**Kind**: init  
**Required**: Yes

Initializes a new anchor by copying custom information from another anchor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(anchor: ARAnchor)
```

#### Discussion

Each time ARKit generates a new [`ARFrame`](arframe.md) object (corresponding to an incoming frame of live camera video at 60 fps), ARKit calls this initializer to copy each of the [`anchors`](arframe/anchors.md) associated with the previous frame.

> **Note**:  ARKit always calls this initializer with an `anchor` parameter of the same class as `self`.

If you subclass [`ARAnchor`](aranchor.md) to add extra properties, your implementation of this initializer should copy the values of those properties, then chain to the superclass initializer. For example, an AR game might define a `BoardAnchor` class to encode the position and size of a game board, so its version of this initializer would copy that `size` property:

```swift
required init(anchor: ARAnchor) {
    let other = anchor as! BoardAnchor
    self.size = other.size
    super.init(anchor: other)
}
```

> ❗ **Important**:  Carefully consider performance and your app’s data model when storing references to other objects in anchors. Copying custom values might be expensive, but multiple references to the same data might or might not be correct for your app

## Parameters

- `anchor`: The other anchor from which to copy information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchorcopying/init(anchor:))*