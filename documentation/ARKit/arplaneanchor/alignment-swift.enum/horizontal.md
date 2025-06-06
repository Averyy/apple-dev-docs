# ARPlaneAnchor.Alignment.horizontal

**Framework**: ARKit  
**Kind**: case

The plane is perpendicular to gravity.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case horizontal
```

#### Discussion

The [`transform`](aranchor/transform.md) property for a horizontal plane anchor includes no rotation about the x- or z-axis. Thus, using this anchor’s transform to place a 3D model asset in your scene results in the model appearing “right side up”.

## See Also

- [ARPlaneAnchor.Alignment.vertical](arplaneanchor/alignment-swift.enum/vertical.md)
  The plane is parallel to gravity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/alignment-swift.enum/horizontal)*