# dataType

**Framework**: Metal  
**Kind**: property

The data format of all elements in the data plane.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var dataType: MTLTensorDataType { get set }
```

#### Discussion

The default value of this property is [`MTLTensorDataType.float32`](mtltensordatatype/float32.md).

[`MTLTensorDataType.metalFloat8ue8m0`](mtltensordatatype/metalfloat8ue8m0.md) is not a valid data type for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/datatype)*