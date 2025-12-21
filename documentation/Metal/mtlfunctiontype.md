# MTLFunctionType

**Framework**: Metal  
**Kind**: enum

The type of a top-level Metal Shading Language (MSL) function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLFunctionType
```

## Topics

### Function types
- [MTLFunctionType.vertex](mtlfunctiontype/vertex.md)
  A vertex function you can use in a render pipeline state object.
- [MTLFunctionType.fragment](mtlfunctiontype/fragment.md)
  A fragment function you can use in a render pipeline state object.
- [MTLFunctionType.kernel](mtlfunctiontype/kernel.md)
  A kernel you can use in a compute pipeline state object.
- [MTLFunctionType.intersection](mtlfunctiontype/intersection.md)
  A function you can use in an intersection function table.
- [MTLFunctionType.visible](mtlfunctiontype/visible.md)
  A function you can use in a visible function table.
### Enumeration Cases
- [MTLFunctionType.mesh](mtlfunctiontype/mesh.md)
- [MTLFunctionType.object](mtlfunctiontype/object.md)
### Initializers
- [init?(rawValue: UInt)](mtlfunctiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var device: any MTLDevice](mtlfunction/device.md)
  The device object that created the shader function.
- [var label: String?](mtlfunction/label.md)
  A string that identifies the shader function.
- [var functionType: MTLFunctionType](mtlfunction/functiontype.md)
  The shader function’s type.
- [var name: String](mtlfunction/name.md)
  The function’s name.
- [var options: MTLFunctionOptions](mtlfunction/options.md)
  The options that Metal used to compile this function.
- [struct MTLFunctionOptions](mtlfunctionoptions.md)
  Options that define how Metal compiles a GPU function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctiontype)*