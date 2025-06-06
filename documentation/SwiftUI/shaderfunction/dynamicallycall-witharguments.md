# dynamicallyCall(withArguments:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new shader by applying the provided argument values to the referenced function.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func dynamicallyCall(withArguments args: [Shader.Argument]) -> Shader
```

#### Discussion

Typically this subscript is used implicitly via function-call syntax, for example:

let shader = ShaderLibrary.default.myFunction(.float(42))

which creates a shader passing the value `42` to the first unbound parameter of `myFunction()`.

## See Also

- [var library: ShaderLibrary](shaderfunction/library.md)
  The shader library storing the function.
- [var name: String](shaderfunction/name.md)
  The name of the shader function in the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shaderfunction/dynamicallycall(witharguments:))*