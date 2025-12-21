# makeFunction(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Synchronously creates an object representing a shader function, using the specified descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction
```

#### Return Value

A new [`MTLFunction`](mtlfunction.md) instance if the method finds the function in the library; otherwise Swift throws an error and Objective-C returns `nil`.

## Parameters

- `descriptor`: The description of the function object to create.

## See Also

- [func makeFunction(name: String) -> (any MTLFunction)?](mtllibrary/makefunction(name:).md)
  Creates an instance that represents a shader function in the library.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](mtllibrary/makefunction(name:constantvalues:completionhandler:).md)
  Asynchronously creates a specialized shader function.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues) throws -> any MTLFunction](mtllibrary/makefunction(name:constantvalues:).md)
  Synchronously creates a specialized shader function.
- [func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](mtllibrary/makefunction(descriptor:completionhandler:).md)
  Asynchronously creates an object representing a shader function, using the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary/makefunction(descriptor:))*