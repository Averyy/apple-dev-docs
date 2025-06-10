# reflection(functionName:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a reflection object for a matching function name in this library instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func reflection(functionName: String) -> MTLFunctionReflection?
```

#### Return Value

An object containing the reflection information, or `nil` if no function in the library matches the name.

## Parameters

- `functionName`: The name of the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary/reflection(functionname:))*