# anchorWithOffset(to:)

**Framework**: UIKit  
**Kind**: method

Creates a layout dimension object from two anchors.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func anchorWithOffset(to otherAnchor: NSLayoutXAxisAnchor) -> NSLayoutDimension
```

#### Return Value

The [`NSLayoutDimension`](nslayoutdimension.md) object represented by the two anchors.

#### Discussion

Use the returned object to define constraints relative to the space between the current anchor and the object in the `otherAnchor` parameter.

## Parameters

- `otherAnchor`: The second anchor to use when creating the layout dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutxaxisanchor/anchorwithoffset(to:))*