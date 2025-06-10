# init(named:in:)

**Framework**: RealityKit  
**Kind**: init

Creates a surface shader object from a named function in a Metal library.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
init(named name: String, in library: any MTLLibrary)
```

#### Discussion

To create a surface shader for a custom material, create a Metal file in your Xcode project. Prefix the function with the keyword `[[visible]]`. The function needs to take a single parameter of type `realitykit::surface_parameters`.

Here’s what a minimal surface shader function looks like:

```cpp
#include <metal_stdlib>
#include <RealityKit/RealityKit.h>

// Specify the current default namespace as metal so our code
// doesn't have to to prefix Metal Standard Library symbols.
using namespace metal;

[[visible]] void mySurfaceShader(realitykit::surface_parameters params) {
   // Calculate parameters needed for rendering.
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
let surfaceShader = CustomMaterial.SurfaceShader(
    named: "mySurfaceShader",
    in: library
)
```

> ❗ **Important**: RealityKit loads surface shader functions by name, so name your surface shader uniquely and to exactly match the `named` parameter.

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## Parameters

- `name`: The name of the surface shader function.
- `library`: The Metal library that contains the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/surfaceshader/init(named:in:))*