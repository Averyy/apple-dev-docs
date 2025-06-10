# instanceDescriptorType

**Framework**: Metal  
**Kind**: property

Controls the type of instance descriptor that the instance descriptor buffer references.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType { get set }
```

#### Discussion

This value determines the layout Metal expects for the structs the instance descriptor buffer contains.

Defaults to `MTLAccelerationStructureInstanceDescriptorTypeIndirect`. Valid values for this property are `MTLAccelerationStructureInstanceDescriptorTypeIndirect` or `MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptortype)*