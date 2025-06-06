# MTLFunctionConstantValues

**Framework**: Metal  
**Kind**: class

A set of constant values that specialize a graphics or compute function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MTLFunctionConstantValues
```

#### Overview

A [`MTLFunctionConstantValues`](mtlfunctionconstantvalues.md) object sets constant values for function constants. Function constants are declared with the `[[ function_constant(index) ]]` attribute in Metal shading language source code. Refer to the [`Metal Shading Language Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364) for more information.

Single constant values can be set individually by index or name. Multiple constant values can be set together with an index range.

A single [`MTLFunctionConstantValues`](mtlfunctionconstantvalues.md) object can be applied to multiple [`MTLFunction`](mtlfunction.md) objects (for example, a vertex function and a fragment function). After a specialized function has been created, any changes to its constant values have no further effect on it. However, you can reset, add, or modify any constant values in the [`MTLFunctionConstantValues`](mtlfunctionconstantvalues.md) object and reuse it to create another [`MTLFunction`](mtlfunction.md) object.

## Topics

### Setting Constant Values
- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, index: Int)](mtlfunctionconstantvalues/setconstantvalue(_:type:index:).md)
  Sets a value for a function constant at a specific index.
- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, withName: String)](mtlfunctionconstantvalues/setconstantvalue(_:type:withname:).md)
  Sets a value for a function constant with a specific name.
- [func setConstantValues(UnsafeRawPointer, type: MTLDataType, range: Range<Int>)](mtlfunctionconstantvalues/setconstantvalues(_:type:range:).md)
  Sets values for a group of function constants within a specific index range.
### Resetting Constant Values
- [func reset()](mtlfunctionconstantvalues/reset.md)
  Deletes all previously set constant values.

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

- [class MTLFunctionConstant](mtlfunctionconstant.md)
  A constant that specializes the behavior of a shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues)*