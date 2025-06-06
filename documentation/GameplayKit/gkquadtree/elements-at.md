# elements(at:)

**Framework**: GameplayKit  
**Kind**: method

Returns all objects whose corresponding locations overlap the specified point.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func elements(at point: vector_float2) -> [ElementType]
```

#### Return Value

An array of all matching elements, or an empty array if no objects are found.

#### Discussion

You specify the point or region corresponding to an object when you add it to the tree with the [`add(_:at:)`](gkquadtree/add(_:at:).md) or [`add(_:in:)`](gkquadtree/add(_:in:).md) method. This method follows the same path down the tree as the two `addElement` methods, but instead of adding a new object to the tree, returns the list of all objects stored in the tree node corresponding to the specified point.

## Parameters

- `point`: The point in 2D space to search.

## See Also

- [func elements(in: GKQuad) -> [ElementType]](gkquadtree/elements(in:).md)
  Returns all objects whose corresponding locations overlap the specified region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkquadtree/elements(at:))*