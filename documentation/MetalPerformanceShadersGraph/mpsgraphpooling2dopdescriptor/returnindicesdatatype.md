# returnIndicesDataType

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

Defines the data type for returned indices. Use this in conjunction with [`maxPooling2DReturnIndices(_:descriptor:name:)`](mpsgraph/maxpooling2dreturnindices(_:descriptor:name:).md) API. Currently MPSGraph supports the following datatypes: `MPSDataTypeInt32`. Default value: `MPSDataTypeInt32`.

**Availability**:
- iOS 15.3+
- iPadOS 15.3+
- Mac Catalyst 15.3+
- macOS 12.2+
- tvOS 15.3+
- visionOS 1.0+

## Declaration

```swift
var returnIndicesDataType: MPSDataType { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling2dopdescriptor/returnindicesdatatype)*