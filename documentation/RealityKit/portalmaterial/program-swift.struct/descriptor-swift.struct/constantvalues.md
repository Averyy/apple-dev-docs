# constantValues

**Framework**: RealityKit  
**Kind**: property

Values for the function-constant inputs that the shader graph declares.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var constantValues: MTLFunctionConstantValues
```

#### Discussion

Function constants are baked into the compiled shader at program creation time and can’t be changed afterward. Use them for values that don’t vary at runtime — for example, a feature flag that selects between two code paths — to eliminate runtime branching and produce a leaner shader. To vary a value across frames or instances, declare it as a regular graph input and supply it through [`inputValues`](portalmaterial/program-swift.struct/descriptor-swift.struct/inputvalues.md) or [`setParameter(name:value:)`](portalmaterial/setparameter(name:value:).md) instead.

Two descriptors that share the same shader graph but differ in their function-constant values produce distinct compiled programs that don’t compare equal.

## See Also

- [var shaderGraph: ShaderGraph](portalmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md)
  The shader graph that describes the shading logic for this program.
- [var inputValues: [String : MaterialParameters.Value]](portalmaterial/program-swift.struct/descriptor-swift.struct/inputvalues.md)
  Initial values for the inputs that the shader graph declares.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/descriptor-swift.struct/constantvalues)*