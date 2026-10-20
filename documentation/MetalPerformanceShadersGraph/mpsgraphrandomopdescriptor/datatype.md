# dataType

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

The data type of the generated result values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var dataType: MPSDataType { get set }
```

```objc
@property (nonatomic, readwrite) MPSDataType dataType;
```

#### Discussion

When sampling from the uniform distribution, valid types are MPSDataTypeFloat16, MPSDataTypeFloat32, and MPSDataTypeInt32. When sampling from the normal or truncated normal distribution, valid types are MPSDataTypeFloat16 and MPSDataTypeFloat32.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomopdescriptor/datatype)*