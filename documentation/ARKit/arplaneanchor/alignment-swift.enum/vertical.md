# ARPlaneAnchor.Alignment.vertical

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

The plane is parallel to gravity.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
case vertical
```

```c
ARPlaneAnchorAlignmentVertical
```

#### Discussion

The [`transform`](../../aranchor/transform.md) property for a vertical plane anchor includes a rotation component. That is, the transform matrix represents the result of rotating a horizontal plane to match the orientation of the detected surface.

## See Also

### Alignment Values
- [ARPlaneAnchor.Alignment.horizontal](./horizontal.md)
  The plane is perpendicular to gravity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/alignment-swift.enum/vertical)*