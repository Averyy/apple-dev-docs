# Passing Structured Data to a Metal Compute Function

**Framework**: RealityKit

Send nontexture data from Swift to your Metal shaders using a shared header file.

#### Overview

[`MTLComputeCommandEncoder`](https://developer.apple.com/documentation/Metal/MTLComputeCommandEncoder) provides [`setTexture(_:index:)`](https://developer.apple.com/documentation/Metal/MTLComputeCommandEncoder/setTexture(_:index:)) to pass image data to a Metal compute function. Compute functions can access those textures using `[[texture(``)]]`. The compute command encoder doesn’t, however, provide an easy way to pass structured data to a compute function. You pass all nonimage data as an unstructured buffer using the encoder’s [`setBytes(_:length:index:)`](https://developer.apple.com/documentation/Metal/MTLComputeCommandEncoder/setBytes(_:length:index:)) methods. It’s possible to use [`setBytes(_:length:index:)`](https://developer.apple.com/documentation/Metal/MTLComputeCommandEncoder/setBytes(_:length:index:)) to pass data contained in a Swift struct to your compute function, which can receive it as a Metal struct as long as the two structs use the same exact memory layout. By using a bridging header and defining the struct in C, Metal and Swift can import the same header file and use the same struct with the same layout in memory.

> **Note**: This article shows how to use a struct contained in a single header file that’s imported by both Swift and Metal. See the <doc:implementing-special-rendering-effects-with-realitykit-postprocessing sample code for two different examples of passing data, one that uses a separate Swift and Metal struct with the same layout in memory, and another that uses the approach from this article.

##### Create a Header File

Create a new header file in your Xcode project. In the file, define a C struct with the properties you need to send from Swift to your Metal compute function. The struct should only contain simple datatypes. Don’t pass textures, samplers, or other complex objects in your struct. Also, don’t use any datatype that doesn’t have a consistent size in both Metal and Swift and on all devices. An `int` datatype, for example, can have different sizes on different devices. Instead, use datatypes like `int32_t`, `uint16_t`, or `float`, which are the same size everywhere.

```occ
#include <simd/simd.h>

#ifndef MyArguments_h
#define MyArguments_h
struct MyArguments
{
    float widgetTolerance
    uint32_t widgetHeight;
};
#endif /* MyArguments_h */
```

##### Import the Struct in a Bridging Header

If your project already has a bridging header, import the struct header file in it. If your project doesn’t have a bridging header, create a new header file in your project to import the struct’s header. By importing using a bridging header, Swift sees the C struct as a Swift struct. Because Metal is a superset of C++, which is a superset of C, Metal interprets the same struct as a Metal struct.

```occ
#import "MyArguments.h"
```

If you created a new bridging header, you must tell Xcode that it’s your project’s bridging header. To do that, go to the build settings for your target and look for a setting called Objective-C Bridging Header. Set it to the path of the bridging header file you created. Don’t use an absolute path. Instead, create a path relative to `$(PROJECT_DIR)`, which points to your project’s main directory. Your entry should look something like this:

```other
$(PROJECT_DIR)/$(PROJECT_NAME)/MyProject-Bridging-Header.h
```

##### Encode the Swift Struct As Bytes

In your Swift code, create an instance of the struct to hold the values to send to your compute function. Then, in the code that dispatches your compute function, call [`setBytes(_:length:index:)`](https://developer.apple.com/documentation/Metal/MTLComputeCommandEncoder/setBytes(_:length:index:)) and pass the struct as a data buffer before you call [`dispatchThreads(_:threadsPerThreadgroup:)`](https://developer.apple.com/documentation/Metal/MTLComputeCommandEncoder/dispatchThreads(_:threadsPerThreadgroup:)) to execute the compute function.

```swift
var args = MyArguments(widgetTolerance: 0.3493, widgetHeight: 5)
encoder.setBytes(&args, length: MemoryLayout<MyArguments>.stride, index: 0)
```

##### Retrieve the Buffer in the Compute Function

In the Metal file that contains your compute function, include the new header file after including .

```other
#include <metal_stdlib>
#include "MyArguments.h" 

using namespace metal;
```

In your compute function, retrieve the buffer using `[[buffer(``)]]` and cast it to your struct. Metal allows you to do that as a function parameter, or you can retrieve it in the body of your function and store it in a variable. Make sure the index value you pass to `[[buffer(``)]]` matches the index value you used in your [`setBytes(_:length:index:)`](https://developer.apple.com/documentation/Metal/MTLComputeCommandEncoder/setBytes(_:length:index:)) call. Your compute function can access members of the retrieved struct using the `->` operator.

```other
[[kernel]]
void myPostProcess(uint2 gid [[thread_position_in_grid]],
                         texture2d<half, access::read> inColor [[texture(0)]],
                         texture2d<half, access::write> outColor [[texture(1)]],
                         constant MyArguments *args [[buffer(0)]])
{
    auto widgetHeight = args->widgetHeight;
    auto widgetTolerance = args->widgetTolerance;

    // Your compute function logic goes here.
}
```

## See Also

- [Using Metal performance shaders to create custom postprocess effects](using-metal-performance-shaders-to-create-custom-postprocess-effects.md)
  Leverage the Metal Performance Shaders framework to create special rendering effects for your RealityKit scenes.
- [Implementing special rendering effects with RealityKit postprocessing](implementing-special-rendering-effects-with-realitykit-postprocessing.md)
  Implement a variety of postprocessing techniques to alter RealityKit rendering.
- [Checking the pixel format of a postprocess effect’s output texture](checking-the-pixel-format-of-a-postprocess-effect-s-output-texture.md)
  Make sure your postprocess effect works on all devices.
- [Implementing postprocess effects using Metal compute functions](implementing-postprocess-effects-using-metal-compute-functions.md)
  Create custom shaders to implement postprocess effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/passing-structured-data-to-a-metal-compute-function)*