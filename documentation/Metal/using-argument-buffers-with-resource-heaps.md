# Using argument buffers with resource heaps

**Framework**: Metal

Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.13+
- tvOS 12.0+
- Xcode 12.3+

#### Overview

In the [`Managing groups of resources with argument buffers`](managing-groups-of-resources-with-argument-buffers.md) sample, you learned how to specify, encode, set, and access resources in an argument buffer.

In this sample, you’ll learn how to combine argument buffers with arrays of resources and resource heaps. In particular, you’ll learn how to define an argument buffer structure that contains arrays and how to allocate and use resources from a heap. The sample renders a static quad that uses multiple resources encoded into an argument buffer.

##### Getting Started

The Xcode project contains schemes for running the sample on macOS, iOS, or tvOS. Metal is not supported in the iOS or tvOS Simulator, so the iOS and tvOS schemes require a physical device to run the sample. The default scheme is macOS, which runs the sample as is on your Mac.

##### Arrays of Arguments in the Metal Shading Language

Arrays can be used as parameters to graphics or compute functions. When a function takes an array as a parameter, the index of the first resource in the array is equal to the base index of the array parameter itself. Thus, each subsequent resource in the array is automatically assigned a subsequent index value, counting incrementally from the base index value.

For example, the following fragment function, `exampleFragmentFunction`, has a parameter, `textureParameters`, that’s an array of 10 textures with a base index value of `5`.

```metal
fragment float4
exampleFragmentFunction(array<texture2d<float>, 10> textureParameters [[ texture(5) ]])
```

Because `textureParameters` has a `[[ texture(5) ]]` attribute qualifier, the corresponding Metal framework method to set this parameter is `setFragmentTexture:atIndex:`, where the values for `index` begin at `5`. Thus, the texture at array index `0` is set at index number `5`, the texture at array index `1` is set at index number `6`, and so on. The last texture in the array, at array index `9`, is set at index number `14`.

##### Define Argument Buffers with Arrays

Arrays can also be used as elements of an argument buffer structure. In this case, the `[[ id(n) ]]` attribute qualifier of an argument buffer behaves the same way as the `[[ texture(n) ]]` attribute qualifier of a function parameter, where `n` is the base index value of the array. However, you don’t call the `setFragmentTexture:atIndex:` method, of a `MTLRenderCommandEncoder` object, to set a texture from the array. Instead, you call the `setTexture:atIndex:` method, of a `MTLArgumentEncoder` object, to encode a texture from the array into the argument buffer, where `index` corresponds to the base index value, `n`,  plus the index of the texture within the array.

The argument buffer in this sample is declared as a `FragmentShaderArguments` structure, and this is its definition:

Each element of this structure uses the `array<T, N>` template, which defines the element as an array of a certain type, `T`, and number of elements, `N`. This argument buffer contains the following resources:

- `exampleTextures`, an array of 32 2D textures with a base index value of `0`.
- `exampleBuffers`, an array of 32 `float` buffers with a base index value of `100`.
- `exampleConstants`, an array of 32 `uint32_t` constants with a base index value of `200`.

![Layout diagram that shows an array of textures, an array of buffers, and an array of constants all encoded into a single argument buffer.](https://docs-assets.developer.apple.com/published/c6d3fcaf3ae4a7586e95129c46cb72a5/argument-buffers-with-heaps-1-ArgumentBufferWithArrays.png)

##### Encode Array Elements Into an Argument Buffer

This sample encodes array elements into an argument buffer by matching the `index` parameter of each `setTexture:atIndex:`, `setBuffer:offset:atIndex:`, and `constantDataAtIndex:` method call to the element’s corresponding index value, defined by the `[[ id(n) ]]` attribute qualifier in the argument buffer.

##### Access Array Elements in an Argument Buffer

Within a function, accessing elements of an array encoded in an argument buffer is the same as accessing elements of a standard array. In this sample, the `exampleTextures`, `exampleBuffers`, and `exampleConstants` arrays are accessed via the `fragmentShaderArgs` parameter of the `fragmentShader` function. Each array element is accessed with the `[n]` subscript syntax, where `n` is the index of the element within the array.

The `fragmentShader` function contains an `if-else` condition that evaluates the `x` component of `texCoord` to determine which side of the quad the fragment is on. If the fragment is on the left side of the quad, the function samples each texture in the `exampleTextures` array and adds the sampled values to determine the final output color.

If the fragment is on right side of the quad, the function reads a value from the `exampleBuffers` array. The function uses the `x` component of `texCoord` to determine which buffer to read from and then uses the `y` component of `texCoord` to determine where in the buffer to read from. The value in the buffer determines the final output color.

##### Combine Argument Buffers with Resource Heaps

The fragment function accesses 32 textures and 32 buffers via the argument buffer, totaling 64 different resources overall. If memory for each of these resources was allocated individually, despite residing in arrays, Metal would need to validate the memory of 64 individual resources before making these resources accessible to the GPU.

Instead, this sample allocates resources from a `MTLHeap` object. A heap is a single memory region from which multiple resources can be allocated. Therefore, the sample can make the heap’s entire memory, including the memory of all the resources within the heap, accessible to the GPU by calling the `useHeap:` method once.

The sample implements a `loadResources` method that loads the resource data into temporary `MTLTexture` and `MTLBuffer` objects. Then, the sample implements a `createHeap` method that calculates the total size required to store the resource data in the heap and creates the heap itself.

The sample implements a `moveResourcesToHeap` method that creates permanent `MTLTexture` and `MTLBuffer` objects allocated from the heap. Then, the method uses a `MTLBlitCommandEncoder` to copy the resource data from the temporary objects to the permanent objects.

Before using these resources, instead of calling the `useResource:usage:` method once for each resource, the sample calls the `useHeap:` method once for the entire heap.

##### Next Steps

In this sample, you learned how to combine argument buffers with arrays of resources and resource heaps. In the [`Encoding argument buffers on the GPU`](encoding-argument-buffers-on-the-gpu.md) sample, you’ll learn how to encode resources into argument buffers with a graphics or compute function.

## See Also

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
  Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md)
  Create argument buffers to organize related resources.
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md)
  Optimize resource performance within an argument buffer.
- [Indexing argument buffers](indexing-argument-buffers.md)
  Assign resource indices within an argument buffer.
- [Rendering terrain dynamically with argument buffers](rendering-terrain-dynamically-with-argument-buffers.md)
  Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding argument buffers on the GPU](encoding-argument-buffers-on-the-gpu.md)
  Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [class MTLArgumentDescriptor](mtlargumentdescriptor.md)
  A representation of an argument within an argument buffer.
- [protocol MTLArgumentEncoder](mtlargumentencoder.md)
  An interface you can use to encode argument data into an argument buffer.
- [var MTLAttributeStrideStatic: Int](mtlattributestridestatic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/using-argument-buffers-with-resource-heaps)*