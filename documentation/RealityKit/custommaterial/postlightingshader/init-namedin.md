# init(named:in:)

**Framework**: RealityKit  
**Kind**: init

Creates a post-lighting shader object from a named function in a Metal library.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
init(named name: String, in library: any MTLLibrary)
```

#### Discussion

To create a post-lighting  shader for a custom material, create a Metal file in your Xcode project. Prefix the function with the keyword `[[stitchable]]`. The function needs to take two parameters, one of type `realitykit::post_lighting_parameters`, and the other an arbitrary pointer to valid data.

Here’s what a minimal post-lighting shader function looks like:

```cpp
#include <metal_stdlib>
#include <RealityKit/RealityKit.h>

// Specify the current default namespace as metal so our code
// doesn't have to to prefix Metal Standard Library symbols.
using namespace metal;

[[stitchable]] void myPostLightingShader(realitykit::post_lighting_parameters params const void *customParams) {
   // Calculate post-lighting effect.
}
```

To create a custom material using this shader, get a reference to your app’s Metal library:

```swift
guard let device = MTLCreateSystemDefaultDevice() else {
    fatalError("Error creating default metal device.")
}
guard let library = maybeDevice.makeDefaultLibrary() else {
    fatalError("Error creating default metal library")
}
```

Once you have a reference to your Metal library, use it to create the surface shader reference:

```swift
let postLightingShader = CustomMaterial.PostLightingShader(
    named: "myPostLightingShader",
    in: library
)
```

> ❗ **Important**: RealityKit loads post-lighting shader functions by name, so name your post-lighting shader uniquely and to exactly match the `named` parameter.

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## Parameters

- `name`: The name of the post-lighting shader function.
- `library`: The Metal library that contains the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/postlightingshader/init(named:in:))*