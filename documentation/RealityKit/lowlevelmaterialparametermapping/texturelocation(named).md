# textureLocation(named:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns the argument table texture slot index for the named texture parameter, or `nil` if no parameter with that name exists.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func textureLocation(named name: String) -> Int?
```

## Return Value

The texture slot index, or `nil` if no texture parameter with that name exists.

## Parameters

- `name`: The name of the texture parameter as declared in the Metal shader.

## See Also

### Locating parameters
- [func bufferLocation(named: String) -> Int?](./bufferlocation%28named%29.md)
  Returns the argument table buffer slot index for the named buffer parameter, or `nil` if no parameter with that name exists.
- [func constantLocation(named: String) -> LowLevelMaterialParameterMapping.ConstantLocation?](./constantlocation%28named%29.md)
  Returns the resolved buffer and constant indices for the named constant parameter, or `nil` if no parameter with that name exists.
- [LowLevelMaterialParameterMapping.ConstantLocation](./constantlocation.md)
  The resolved buffer and constant slot indices for a named constant parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/texturelocation(named:))*