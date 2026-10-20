# makeFunction(descriptor:completionHandler:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously creates an object representing a shader function, using the specified descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: @escaping @Sendable ((any MTLFunction)?, (any Error)?) -> Void)
```

```swift
func makeFunction(descriptor: MTLFunctionDescriptor) async throws -> any MTLFunction
```

```objc
- (void) newFunctionWithDescriptor:(MTLFunctionDescriptor *) descriptor completionHandler:(void (^)(id<MTLFunction>function, NSError *error)) completionHandler;
```

## Parameters

- `descriptor`: The description of the function object to create.
- `completionHandler`: A Swift closure or an Objective-C block that Metal calls after it creates the function.

## See Also

### Creating shader function instances
- [func makeFunction(name: String) -> (any MTLFunction)?](./makefunction%28name%29.md)
  Creates an instance that represents a shader function in the library.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](./makefunction%28name,constantvalues,completionhandler%29.md)
  Asynchronously creates a specialized shader function.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues) throws -> any MTLFunction](./makefunction%28name,constantvalues%29.md)
  Synchronously creates a specialized shader function.
- [func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction](./makefunction%28descriptor%29.md)
  Synchronously creates an object representing a shader function, using the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary/makefunction(descriptor:completionhandler:))*