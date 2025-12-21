# MTLLinkedFunctions

**Framework**: Metal  
**Kind**: class

A set of related functions that Metal links to when necessary to create the function instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLLinkedFunctions
```

#### Overview

When you create a Metal function instance using an [`MTLFunctionDescriptor`](mtlfunctiondescriptor.md), you specify additional functions that Metal needs to link to when it compiles and links the underlying shader code. Most often, you need to do this if your shader takes a visible function table as one or more of its arguments. For Metal to create the [`MTLFunction`](mtlfunction.md) instance, it needs a complete list of functions that your shader can call so that it can resolve any dependencies and generate the correct code to run on the GPU.

## Topics

### Specifying related functions
- [var functions: [any MTLFunction]?](mtllinkedfunctions/functions.md)
  An array of function objects to link to the new function.
- [var binaryFunctions: [any MTLFunction]?](mtllinkedfunctions/binaryfunctions.md)
  An array of function objects already compiled to a binary representation to link.
- [var groups: [String : [any MTLFunction]]?](mtllinkedfunctions/groups.md)
  An optional list of groups specifying which functions your shader can call at each call site.
- [var privateFunctions: [any MTLFunction]?](mtllinkedfunctions/privatefunctions.md)
  An array of function objects to link to the new function, without exporting the functions publicly.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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
  Options that define how Metal compiles a GPU function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllinkedfunctions)*