# LowLevelMaterialParameterMapping.ConstantLocation

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The resolved buffer and constant slot indices for a named constant parameter.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ConstantLocation
```

## Topics

### Accessing the constant index
- [var constantIndex: Int](./constantlocation/constantindex.md)
  The index of the constant within the buffer slot’s constant array.
### Instance Properties
- [var bufferIndex: Int](./constantlocation/bufferindex.md)
  The buffer slot index within the argument table.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Locating parameters
- [func bufferLocation(named: String) -> Int?](./bufferlocation%28named%29.md)
  Returns the argument table buffer slot index for the named buffer parameter, or `nil` if no parameter with that name exists.
- [func textureLocation(named: String) -> Int?](./texturelocation%28named%29.md)
  Returns the argument table texture slot index for the named texture parameter, or `nil` if no parameter with that name exists.
- [func constantLocation(named: String) -> LowLevelMaterialParameterMapping.ConstantLocation?](./constantlocation%28named%29.md)
  Returns the resolved buffer and constant indices for the named constant parameter, or `nil` if no parameter with that name exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/constantlocation)*