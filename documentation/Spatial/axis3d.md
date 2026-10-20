# Axis3D

**Framework**: Spatial  
**Kind**: struct  
**Role**: Structure

Constants that describe an axis.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct Axis3D
```

```c
typedef enum { ... } SPAxis;
```

## Topics

### Constants
- [static var x: Axis3D](./axis3d/x.md)
  The operation is along the x-axis.
- [static var y: Axis3D](./axis3d/y.md)
  The operation is along the y-axis.
- [static var z: Axis3D](./axis3d/z.md)
### Initializers
- [init(UInt32)](./axis3d/init%28_%29.md)
  Creates a new 3D axis structure.
- [init(rawValue: UInt32)](./axis3d/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
### Inspecting the axis
- [var rawValue: UInt32](./axis3d/rawvalue.md)
  The corresponding value of the raw type.
### Default Implementations
- [Decodable Implementations](./axis3d/decodable-implementations.md)
- [Encodable Implementations](./axis3d/encodable-implementations.md)
- [Hashable Implementations](./axis3d/hashable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data structures
- [struct Vector3D](./vector3d.md)
  A three-element vector.
- [struct Vector3DFloat](./vector3dfloat.md)
  A single-precision structure that defines a three-element vector


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/axis3d)*