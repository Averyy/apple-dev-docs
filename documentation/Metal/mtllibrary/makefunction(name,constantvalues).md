# makeFunction(name:constantValues:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Synchronously creates a specialized shader function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func makeFunction(name: String, constantValues: MTLFunctionConstantValues) throws -> any MTLFunction
```

```objc
- (id<MTLFunction>) newFunctionWithName:(NSString *) name constantValues:(MTLFunctionConstantValues *) constantValues error:(NSError **) error;
```

## Return Value

A new [`MTLFunction`](../mtlfunction.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Function constant values are first looked up by their index, then by their name. The compiler ignores any values that don’t correspond to a function constant in the named function, and doesn’t generate errors or warnings.

## Parameters

- `name`: The name of the specialized function.
- `constantValues`: The set of constant values for the function constants. The compiler can’t compile the function if any value is invalid for the function constants it requires.

## See Also

### Creating shader function instances
- [func makeFunction(name: String) -> (any MTLFunction)?](./makefunction%28name%29.md)
  Creates an instance that represents a shader function in the library.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](./makefunction%28name,constantvalues,completionhandler%29.md)
  Asynchronously creates a specialized shader function.
- [func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](./makefunction%28descriptor,completionhandler%29.md)
  Asynchronously creates an object representing a shader function, using the specified descriptor.
- [func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction](./makefunction%28descriptor%29.md)
  Synchronously creates an object representing a shader function, using the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary/makefunction(name:constantvalues:))*