# MTLFunctionDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

A description of a function object to create.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLFunctionDescriptor
```

```objc
@interface MTLFunctionDescriptor : NSObject
```

## Mentions

- [Compiling binary archives from a custom configuration script](./compiling-binary-archives-from-a-custom-configuration-script.md)

## Topics

### Specifying the function configuration
- [var name: String?](./mtlfunctiondescriptor/name.md)
  The name of the function to fetch from the library.
- [var specializedName: String?](./mtlfunctiondescriptor/specializedname.md)
  A new name for the created function object.
- [var constantValues: MTLFunctionConstantValues?](./mtlfunctiondescriptor/constantvalues.md)
  The set of constant values assigned to the function constants.
- [var options: MTLFunctionOptions](./mtlfunctiondescriptor/options.md)
  Flags specifying how Metal should create the new function object.
- [var binaryArchives: [any MTLBinaryArchive]?](./mtlfunctiondescriptor/binaryarchives.md)
  The binary archives to search for a previously-compiled version of this function.
- [struct MTLFunctionOptions](./mtlfunctionoptions.md)
  Options that define how Metal compiles a GPU function.
- [class MTLLinkedFunctions](./mtllinkedfunctions.md)
  A set of related functions that Metal links to when necessary to create the function instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MTLIntersectionFunctionDescriptor](./mtlintersectionfunctiondescriptor.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](./mtllibrary/makefunction%28descriptor,completionhandler%29.md)
  Asynchronously creates an object representing a shader function, using the specified descriptor.
- [func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction](./mtllibrary/makefunction%28descriptor%29.md)
  Synchronously creates an object representing a shader function, using the specified descriptor.
### Shader functions
- [protocol MTLFunction](./mtlfunction.md)
  A interface that represents a public shader function in a Metal library.
- [protocol MTLFunctionHandle](./mtlfunctionhandle.md)
  An object representing a function that you can add to a visible function table.
- [class MTLVisibleFunctionTableDescriptor](./mtlvisiblefunctiontabledescriptor.md)
  A specification of how to create a visible function table.
- [protocol MTLVisibleFunctionTable](./mtlvisiblefunctiontable.md)
  A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.
- [class MTLIntersectionFunctionDescriptor](./mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [class MTLIntersectionFunctionTableDescriptor](./mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [protocol MTLIntersectionFunctionTable](./mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctiondescriptor)*