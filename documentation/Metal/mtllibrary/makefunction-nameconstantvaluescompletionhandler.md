# makeFunction(name:constantValues:completionHandler:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Asynchronously creates a specialized shader function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func makeFunction(name: String, constantValues: MTLFunctionConstantValues) async throws -> any MTLFunction
```

#### Discussion

Function constant values are first looked up by their index, then by their name. Metal ignores any values that don’t correspond to a function constant in the named function without generating errors or warnings.

## Parameters

- `name`: The name of the specialized function.
- `constantValues`: The set of constant values assigned to the function constants. Compilation fails if you don’t provide valid constant values for all required function constants.
- `completionHandler`: A block of code that Metal calls after it creates the specialized function.

## See Also

- [func makeFunction(name: String) -> (any MTLFunction)?](mtllibrary/makefunction(name:).md)
  Creates an instance that represents a shader function in the library.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues) throws -> any MTLFunction](mtllibrary/makefunction(name:constantvalues:).md)
  Synchronously creates a specialized shader function.
- [func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](mtllibrary/makefunction(descriptor:completionhandler:).md)
  Asynchronously creates an object representing a shader function, using the specified descriptor.
- [func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction](mtllibrary/makefunction(descriptor:).md)
  Synchronously creates an object representing a shader function, using the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary/makefunction(name:constantvalues:completionhandler:))*