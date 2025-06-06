# init(named:in:constantValues:)

**Framework**: RealityKit  
**Kind**: init

Creates a surface shader with the specified function constant values.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
init(named name: String, in library: any MTLLibrary, constantValues: MTLFunctionConstantValues)
```

#### Discussion

Function constants allow you to better share code or toggle features in your shaders without runtime performance costs by resolving their values at compile time.

To use function constants, first define them within your metal code:

```cpp
constant bool kEnableBasicLighting [[function_constant(0)]];

[[stitchable]]
void surfaceShader(realitykit::surface_parameters params) {
    float3 baseColor = float3(1,0,0);
    if (kEnableBasicLighting) {
        float3 lighting = params.geometry().normal() * params.geometry().view_direction() * baseColor;
        params.surface().set_emissive_color(half3(lighting));
    } else {
        params.surface().set_emissive_color(half3(baseColor));
    }
}
```

Then initialize a surface shader with a `Metal/MTLFunctionConstantValues` object that defines values for your constants.

```swift
let constants = MTLFunctionConstantValues()
var yes = true
funcConstants.setConstantValue(&yes, type: .bool, index: 0)

let geom = CustomMaterial.SurfaceShader.init(named: "surfaceShader", in: library, constantValues: constants)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/surfaceshader/init(named:in:constantvalues:))*