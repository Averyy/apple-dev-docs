# constantLocation(named:)

**Framework**: RealityKit  
**Kind**: method

Returns the resolved buffer and constant indices for the named constant parameter, or `nil` if no parameter with that name exists.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func constantLocation(named name: String) -> LowLevelMaterialParameterMapping.ConstantLocation?
```

#### Return Value

A [`LowLevelMaterialParameterMapping.ConstantLocation`](lowlevelmaterialparametermapping/constantlocation.md) with the buffer and constant indices, or `nil` if no constant parameter with that name exists.

## Parameters

- `name`: The name of the constant parameter as declared in the Metal shader.

## See Also

- [func bufferLocation(named: String) -> Int?](lowlevelmaterialparametermapping/bufferlocation(named:).md)
  Returns the argument table buffer slot index for the named buffer parameter, or `nil` if no parameter with that name exists.
- [func textureLocation(named: String) -> Int?](lowlevelmaterialparametermapping/texturelocation(named:).md)
  Returns the argument table texture slot index for the named texture parameter, or `nil` if no parameter with that name exists.
- [LowLevelMaterialParameterMapping.ConstantLocation](lowlevelmaterialparametermapping/constantlocation.md)
  The resolved buffer and constant slot indices for a named constant parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/constantlocation(named:))*