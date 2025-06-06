# ARPlaneAnchor.Alignment.vertical

**Framework**: ARKit  
**Kind**: case

The plane is parallel to gravity.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
case vertical
```

#### Discussion

The [`transform`](aranchor/transform.md) property for a vertical plane anchor includes a rotation component. That is, the transform matrix represents the result of rotating a horizontal plane to match the orientation of the detected surface.

## See Also

- [ARPlaneAnchor.Alignment.horizontal](arplaneanchor/alignment-swift.enum/horizontal.md)
  The plane is perpendicular to gravity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/alignment-swift.enum/vertical)*