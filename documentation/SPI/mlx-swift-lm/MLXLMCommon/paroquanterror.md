---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/paroquanterror"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ParoQuantError

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

## Declaration

```swift
enum ParoQuantError
```

## Topics

### Enumeration Cases
- [case invalidTensorShape(key: String, expected: [Int], actual: [Int])](./paroquanterror/invalidtensorshape%28key,expected,actual%29.md)
- [ParoQuantError.missingConfig](./paroquanterror/missingconfig.md)
- [ParoQuantError.missingTensor(_:)](./paroquanterror/missingtensor%28_%29.md)
- [ParoQuantError.rotationLayerNotFound(_:)](./paroquanterror/rotationlayernotfound%28_%29.md)
- [ParoQuantError.rotationLayerPatchFailed(_:)](./paroquanterror/rotationlayerpatchfailed%28_%29.md)
- [case rotationLayerTypeMismatch(path: String, actualType: String)](./paroquanterror/rotationlayertypemismatch%28path,actualtype%29.md)
- [ParoQuantError.unsupportedModel](./paroquanterror/unsupportedmodel.md)
- [case unsupportedRotationGeometry(path: String, reason: String)](./paroquanterror/unsupportedrotationgeometry%28path,reason%29.md)
### Instance Properties
- [var errorDescription: String?](./paroquanterror/errordescription.md)
### Default Implementations
- [Error Implementations](./paroquanterror/error-implementations.md)
- [LocalizedError Implementations](./paroquanterror/localizederror-implementations.md)

## Relationships

### Conforms To
- Foundation.LocalizedError
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/paroquanterror)*