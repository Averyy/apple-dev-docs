# model

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The object detector’s underlying Core ML model instance.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var model: MLModel { get }
```

#### Discussion

> **Note**: This computed property exports and compiles a Core ML model. Prefer storing the result to using this property repeatedly.

## See Also

### Inspecting an object detector model
- [let modelParameters: MLObjectDetector.ModelParameters](./modelparameters-swift.property.md)
  The model configuration parameters the object detector used during its training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/model)*