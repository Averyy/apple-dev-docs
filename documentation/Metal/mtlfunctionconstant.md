# MTLFunctionConstant

**Framework**: Metal  
**Kind**: class

A constant that specializes the behavior of a shader.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MTLFunctionConstant
```

#### Overview

Don’t create an [`MTLFunctionConstant`](mtlfunctionconstant.md) instance directly. Instead, the list of function constants for a function by querying the `functionConstants` property of an [`MTLFunction`](mtlfunction.md) instance.

An [`MTLFunctionConstant`](mtlfunctionconstant.md) instance should only be obtained from a nonspecialized function created with the [`makeFunction(name:)`](mtllibrary/makefunction(name:).md) method. You only need an [`MTLFunctionConstant`](mtlfunctionconstant.md) instance if you don’t have sufficient information to create an [`MTLFunctionConstantValues`](mtlfunctionconstantvalues.md) instance used to create a specialized function with the [`makeFunction(name:constantValues:)`](mtllibrary/makefunction(name:constantvalues:).md) or [`makeFunction(name:constantValues:completionHandler:)`](mtllibrary/makefunction(name:constantvalues:completionhandler:).md) method.

## Topics

### Reading the function constant’s properties
- [var name: String](mtlfunctionconstant/name.md)
  The name of the function constant.
- [var type: MTLDataType](mtlfunctionconstant/type.md)
  The data type of the function constant.
- [var index: Int](mtlfunctionconstant/index.md)
  The index of the function constant.
- [var required: Bool](mtlfunctionconstant/required.md)
  A Boolean value indicating whether the function constant needs to be provided to specialize the function.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLFunctionConstantValues](mtlfunctionconstantvalues.md)
  A set of constant values that specialize a graphics or compute GPU function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionconstant)*