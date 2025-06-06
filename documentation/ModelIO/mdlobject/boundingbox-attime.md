# boundingBox(atTime:)

**Framework**: Model I/O  
**Kind**: method

Returns the minimum region entirely enclosing the object’s contents at the specified time sample.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func boundingBox(atTime time: TimeInterval) -> MDLAxisAlignedBoundingBox
```

#### Return Value

The asset’s bounding box as of the specified time sample.

#### Discussion

Objects may or may not provide spatial content. Subclasses of [`MDLObject`](mdlobject.md) that include spatial content, such as the [`MDLMesh`](mdlmesh.md) class, implement this method to return the axis-aligned minimal region that entirely encloses such content. Objects without spatial content return an empty bounding box—that is, a [`MDLAxisAlignedBoundingBox`](mdlaxisalignedboundingbox.md) structure whose `minBounds` field is greater than its `maxBounds` field.

Calling this method on an object that contains other objects (that is, one whose [`children`](mdlobject/children.md) property is not `nil` and references a nonempty container) recursively computes the combined bounding box enclosing of the object’s children.

## Parameters

- `time`: A timestamp referring to timed information in the asset.

## See Also

- [var transform: (any MDLTransformComponent)?](mdlobject/transform.md)
  A component that manages this object’s spatial transform and its changes over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/boundingbox(attime:))*