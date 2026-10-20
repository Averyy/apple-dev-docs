# argumentTableDescriptor

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The argument table descriptor that describes the buffer and texture slots this function requires, or `nil` if the function takes no per-draw arguments.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var argumentTableDescriptor: LowLevelArgumentTable.Descriptor? { get }
```

## See Also

### Configuring the function
- [var parameterMapping: LowLevelMaterialParameterMapping?](./parametermapping.md)
  The parameter name-to-slot mapping for this function, used to look up binding indices by name at runtime, or `nil` if the function takes no custom parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/function/argumenttabledescriptor)*