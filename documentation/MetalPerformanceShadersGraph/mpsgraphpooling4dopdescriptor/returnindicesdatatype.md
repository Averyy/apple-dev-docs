# returnIndicesDataType

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

Defines the data type for returned indices.

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

```objc
@property (nonatomic, readwrite) MPSDataType returnIndicesDataType;
```

#### Discussion

Use this in conjunction with [`maxPooling4DReturnIndices(_:descriptor:name:)`](../mpsgraph/maxpooling4dreturnindices%28_,descriptor,name%29.md) API. Currently MPSGraph supports the following datatypes: `MPSDataTypeInt32`. Default value: `MPSDataTypeInt32`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor/returnindicesdatatype)*