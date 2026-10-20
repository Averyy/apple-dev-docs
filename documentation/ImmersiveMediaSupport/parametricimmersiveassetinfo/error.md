# ParametricImmersiveAssetInfo.Error

**Framework**: Immersive Media Support  
**Kind**: struct  
**Role**: Structure

An error that occurs during the conversion process of the parametric immersive asset.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Error
```

## Topics

### Instance Properties
- [var errorDescription: String?](./error/errordescription.md)
  A description of what went wrong, for debugging purposes.
- [let errorType: ParametricImmersiveAssetInfo.Error.ErrorType](./error/errortype-swift.property.md)
  An error type that describes this error.
### Enumerations
- [ParametricImmersiveAssetInfo.Error.ErrorType](./error/errortype-swift.enum.md)
  A type of an error that may occur when converting the original wide field of view video asset to a parametric immersive asset.

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo/error)*