# type

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

Provide a unique identifier for type of deformer. There can only be one `deform` function associated with each type String. However, each `deform` can vary greatly based on run time options and input.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var type: String { get }
```

## Default Implementations

### MeshDeformer Implementations
- [var type: String](./type-8vjw9.md)
  default implementation provided, returns `Self.type`

## See Also

### Identifying the deformer
- [var type: String](./type-nxsx.md)
  provide a unique identifier for type of deformer, default implementation provided


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformer/type-swift.type.property)*