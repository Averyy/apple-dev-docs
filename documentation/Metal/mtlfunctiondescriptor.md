# MTLFunctionDescriptor

**Framework**: Metal  
**Kind**: class

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

## Mentions

- [Compiling Binary Archives from a Custom Configuration Script](compiling-binary-archives-from-a-custom-configuration-script.md)

## Topics

### Specifying the Function Configuration
- [var name: String?](mtlfunctiondescriptor/name.md)
  The name of the function to fetch from the library.
- [var specializedName: String?](mtlfunctiondescriptor/specializedname.md)
  A new name for the created function object.
- [var constantValues: MTLFunctionConstantValues?](mtlfunctiondescriptor/constantvalues.md)
  The set of constant values assigned to the function constants.
- [var options: MTLFunctionOptions](mtlfunctiondescriptor/options.md)
  Flags specifying how Metal should create the new function object.
- [var binaryArchives: [any MTLBinaryArchive]?](mtlfunctiondescriptor/binaryarchives.md)
  The binary archives to search for a previously-compiled version of this function.
- [struct MTLFunctionOptions](mtlfunctionoptions.md)
  Options that define how Metal creates the function object.
- [class MTLLinkedFunctions](mtllinkedfunctions.md)
  A set of related functions that Metal links to when necessary to create the function object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](mtllibrary/makefunction(descriptor:completionhandler:).md)
  Asynchronously creates an object representing a shader function, using the specified descriptor.
- [func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction](mtllibrary/makefunction(descriptor:).md)
  Synchronously creates an object representing a shader function, using the specified descriptor.
- [protocol MTLFunction](mtlfunction.md)
  An object that represents a public shader function in a Metal library.
- [protocol MTLFunctionHandle](mtlfunctionhandle.md)
  An object representing a function that you can add to a visible function table.
- [class MTLVisibleFunctionTableDescriptor](mtlvisiblefunctiontabledescriptor.md)
  A specification of how to create a visible function table.
- [protocol MTLVisibleFunctionTable](mtlvisiblefunctiontable.md)
  A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.
- [class MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [class MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [protocol MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctiondescriptor)*