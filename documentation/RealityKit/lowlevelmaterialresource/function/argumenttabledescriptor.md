# argumentTableDescriptor

**Framework**: RealityKit  
**Kind**: property  
**Required**: Yes

The argument table descriptor that describes the buffer and texture slots this function requires, or `nil` if the function takes no per-draw arguments.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var argumentTableDescriptor: LowLevelArgumentTable.Descriptor? { get }
```

## See Also

- [var parameterMapping: LowLevelMaterialParameterMapping?](lowlevelmaterialresource/function/parametermapping.md)
  The parameter name-to-slot mapping for this function, used to look up binding indices by name at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/function/argumenttabledescriptor)*