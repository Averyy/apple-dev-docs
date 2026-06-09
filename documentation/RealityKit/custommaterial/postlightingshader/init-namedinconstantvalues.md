# init(named:in:constantValues:)

**Framework**: RealityKit  
**Kind**: init

Creates a post-lighting shader with the specified function constant values.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
init(named name: String, in library: any MTLLibrary, constantValues: MTLFunctionConstantValues)
```

#### Discussion

Function constants allow you to better share code or toggle features in your shaders without runtime performance costs by resolving their values at compile time.

To use function constants, first define them within your metal code:

```cpp

constant uint32_t kChannelIndex [[function_constant(0)]];

[[stitchable]]
void postLightingShader(realitykit::post_lighting_parameters params, constant void *customParams) RK_AVAILABILITY_IOS_27 RK_AVAILABILITY_MACOS_27
{
   if (kChannelIndex < 4) {
       half4 color = params.lighting().color();
       color.rgb = color[kChannelIndex];
       color.a = 1.0h;
       params.lighting().set_color(color);
   }
}
```

Then initialize a post-lighting shader with a `Metal/MTLFunctionConstantValues` object that defines values for your constants.

```swift
let constants = MTLFunctionConstantValues()
var channelIndex : UInt32 = 3
funcConstants.setConstantValue(&channelIndex, type: .uint, index: 0)

let postLighting = CustomMaterial.PostLightingShader.init(named: "postLightingShader", in: library, constantValues: constants)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/postlightingshader/init(named:in:constantvalues:))*