# lookingAt(_:)

**Framework**: Group Activities  
**Kind**: method

Creates a direction that orients the participant to face another template element.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func lookingAt(_ element: any SpatialTemplateElement) -> SpatialTemplateElementDirection
```

#### Return Value

A direction type that faces the specified seat position.

#### Discussion

Call this method when you want one participant to look at another participant.

## Parameters

- `element`: The template element to look at.

## See Also

- [static func lookingAt(SpatialTemplateElementPosition) -> SpatialTemplateElementDirection](spatialtemplateelementdirection/lookingat(_:)-1d7ak.md)
  Creates a direction that orients the participant to face the specified point in the shared coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateelementdirection/lookingat(_:)-70j0i)*