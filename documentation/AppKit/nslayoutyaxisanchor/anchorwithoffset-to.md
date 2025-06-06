# anchorWithOffset(to:)

**Framework**: AppKit  
**Kind**: method

Creates a layout dimension object from two anchors.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func anchorWithOffset(to otherAnchor: NSLayoutYAxisAnchor) -> NSLayoutDimension
```

#### Return Value

The [`NSLayoutDimension`](nslayoutdimension.md) object represented by the two anchors.

#### Discussion

Use the returned object to define constraints relative to the space between the current anchor and the object in the `otherAnchor` parameter.

## Parameters

- `otherAnchor`: The second anchor to use when creating the layout dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutyaxisanchor/anchorwithoffset(to:))*