# LowLevelMeshInstance.SortCategory

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The sort category of this mesh instance.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum SortCategory
```

## Topics

### Identifying sort categories
- [LowLevelMeshInstance.SortCategory.opaque](./sortcategory-swift.enum/opaque.md)
  An opaque draw call that renders before all transparent instances.
- [LowLevelMeshInstance.SortCategory.transparent](./sortcategory-swift.enum/transparent.md)
  A transparent draw call sorted back-to-front by distance from the camera.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sorting instances
- [var sortCategory: LowLevelMeshInstance.SortCategory](./sortcategory-swift.property.md)
  The sort category of this mesh instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshinstance/sortcategory-swift.enum)*