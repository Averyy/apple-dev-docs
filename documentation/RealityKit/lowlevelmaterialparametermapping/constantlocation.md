# LowLevelMaterialParameterMapping.ConstantLocation

**Framework**: RealityKit  
**Kind**: struct

The resolved buffer and constant slot indices for a named constant parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ConstantLocation
```

## Topics

### Accessing the constant index
- [var constantIndex: Int](lowlevelmaterialparametermapping/constantlocation/constantindex.md)
  The index of the constant within the buffer slot’s constant array.
### Instance Properties
- [var bufferIndex: Int](lowlevelmaterialparametermapping/constantlocation/bufferindex.md)
  The buffer slot index within the argument table.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func bufferLocation(named: String) -> Int?](lowlevelmaterialparametermapping/bufferlocation(named:).md)
  Returns the argument table buffer slot index for the named buffer parameter, or `nil` if no parameter with that name exists.
- [func textureLocation(named: String) -> Int?](lowlevelmaterialparametermapping/texturelocation(named:).md)
  Returns the argument table texture slot index for the named texture parameter, or `nil` if no parameter with that name exists.
- [func constantLocation(named: String) -> LowLevelMaterialParameterMapping.ConstantLocation?](lowlevelmaterialparametermapping/constantlocation(named:).md)
  Returns the resolved buffer and constant indices for the named constant parameter, or `nil` if no parameter with that name exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/constantlocation)*