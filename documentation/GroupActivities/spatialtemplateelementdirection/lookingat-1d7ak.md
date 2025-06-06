# lookingAt(_:)

**Framework**: Group Activities  
**Kind**: method

Creates a direction that orients the participant to face the specified point in the shared coordinate space.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func lookingAt(_ position: SpatialTemplateElementPosition) -> SpatialTemplateElementDirection
```

#### Return Value

A direction type that faces the specified position in the coordinate space.

## Parameters

- `position`: A location in the shared coordinate space. Specify   positions as an offset from the app’s content using the    type.

## See Also

- [static func lookingAt(any SpatialTemplateElement) -> SpatialTemplateElementDirection](spatialtemplateelementdirection/lookingat(_:)-70j0i.md)
  Creates a direction that orients the participant to face another template element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateelementdirection/lookingat(_:)-1d7ak)*