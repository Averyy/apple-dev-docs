# makeFunction(name:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates an instance that represents a shader function in the library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeFunction(name functionName: String) -> (any MTLFunction)?
```

#### Return Value

An [`MTLFunction`](mtlfunction.md), or `nil` if the named function isn’t found in the library.

#### Discussion

If you call this method to retrieve a function that doesn’t use function constants, it returns an [`MTLFunction`](mtlfunction.md) instance that you can use to build a render or compute pipeline.

If you call this method to retrieve a function that uses function constants to specialize its behavior, you can only use the returned instance to query the `functionConstants` property for the list of function constants. You can’t use to create a render or compute pipeline. To get a specialized instance that you can use to create a pipeline instance, call the [`makeFunction(name:constantValues:completionHandler:)`](mtllibrary/makefunction(name:constantvalues:completionhandler:).md) method or [`makeFunction(name:constantValues:)`](mtllibrary/makefunction(name:constantvalues:).md) to generate a specialized function.

## Parameters

- `functionName`: The name of the function.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](mtllibrary/makefunction(name:constantvalues:completionhandler:).md)
  Asynchronously creates a specialized shader function.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues) throws -> any MTLFunction](mtllibrary/makefunction(name:constantvalues:).md)
  Synchronously creates a specialized shader function.
- [func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](mtllibrary/makefunction(descriptor:completionhandler:).md)
  Asynchronously creates an object representing a shader function, using the specified descriptor.
- [func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction](mtllibrary/makefunction(descriptor:).md)
  Synchronously creates an object representing a shader function, using the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary/makefunction(name:))*