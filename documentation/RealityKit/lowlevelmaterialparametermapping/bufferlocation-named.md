# bufferLocation(named:)

**Framework**: RealityKit  
**Kind**: method

Returns the argument table buffer slot index for the named buffer parameter, or `nil` if no parameter with that name exists.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func bufferLocation(named name: String) -> Int?
```

#### Return Value

The buffer slot index, or `nil` if no buffer parameter with that name exists.

## Parameters

- `name`: The name of the buffer parameter as declared in the Metal shader.

## See Also

- [func textureLocation(named: String) -> Int?](lowlevelmaterialparametermapping/texturelocation(named:).md)
  Returns the argument table texture slot index for the named texture parameter, or `nil` if no parameter with that name exists.
- [func constantLocation(named: String) -> LowLevelMaterialParameterMapping.ConstantLocation?](lowlevelmaterialparametermapping/constantlocation(named:).md)
  Returns the resolved buffer and constant indices for the named constant parameter, or `nil` if no parameter with that name exists.
- [LowLevelMaterialParameterMapping.ConstantLocation](lowlevelmaterialparametermapping/constantlocation.md)
  The resolved buffer and constant slot indices for a named constant parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/bufferlocation(named:))*