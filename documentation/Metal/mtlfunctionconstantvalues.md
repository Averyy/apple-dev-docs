# MTLFunctionConstantValues

**Framework**: Metal  
**Kind**: class

A set of constant values that specialize a graphics or compute GPU function.

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

An [`MTLFunctionConstantValues`](mtlfunctionconstantvalues.md) instance sets constant values for function constants. You declare function constants with the `[[ function_constant(index) ]]` attribute in MSL (Metal Shading Language) source code. See the [`Metal Shading Language specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) for more information.

With an [`MTLFunctionConstantValues`](mtlfunctionconstantvalues.md) instance, you can set each constant value individually with an index or a name, or set multiple constant values with an index range.

You can apply a single [`MTLFunctionConstantValues`](mtlfunctionconstantvalues.md) instance to multiple [`MTLFunction`](mtlfunction.md) instances of any kind, such as a vertex function and a fragment function. When you create a specialized function, subsequent changes to its constant values have no effect. However, you can reset, add, or modify a constant value in your [`MTLFunctionConstantValues`](mtlfunctionconstantvalues.md) instance and reuse it to create another [`MTLFunction`](mtlfunction.md) instance.

> 💡 **Tip**:  See [`Using function specialization to build pipeline variants`](using-function-specialization-to-build-pipeline-variants.md) for a sample code project that applies function constant values.

## Topics

### Setting constant values
- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, index: Int)](mtlfunctionconstantvalues/setconstantvalue(_:type:index:).md)
  Sets a value for a function constant at a specific index.
- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, withName: String)](mtlfunctionconstantvalues/setconstantvalue(_:type:withname:).md)
  Sets a value for a function constant with a specific name.
- [func setConstantValues(UnsafeRawPointer, type: MTLDataType, range: Range<Int>)](mtlfunctionconstantvalues/setconstantvalues(_:type:range:).md)
  Sets values for a group of function constants within a specific index range.
### Resetting constant values
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