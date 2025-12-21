# instanceDescriptorType

**Framework**: Metal  
**Kind**: property

Controls the type of instance descriptor that the instance descriptor buffer references.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType { get set }
```

#### Discussion

This value determines the layout Metal expects for the structs the instance descriptor buffer contains.

Defaults to `MTLAccelerationStructureInstanceDescriptorTypeIndirect`. Valid values for this property are `MTLAccelerationStructureInstanceDescriptorTypeIndirect` or `MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptortype)*