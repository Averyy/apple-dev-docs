# setConstantValue(_:type:index:)

**Framework**: Metal  
**Kind**: method

Sets a value for a function constant at a specific index.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setConstantValue(_ value: UnsafeRawPointer, type: MTLDataType, index: Int)
```

#### Discussion

Declare a single function constant in Metal Shading Language (MSL).

```metal
constant bool a [[ function_constant(0) ]];
```

Set its value by assigning with a specific index.

## Parameters

- `value`: A pointer to the constant value.
- `type`: The data type of the function constant.
- `index`: The index of the function constant.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, withName: String)](mtlfunctionconstantvalues/setconstantvalue(_:type:withname:).md)
  Sets a value for a function constant with a specific name.
- [func setConstantValues(UnsafeRawPointer, type: MTLDataType, range: Range<Int>)](mtlfunctionconstantvalues/setconstantvalues(_:type:range:).md)
  Sets values for a group of function constants within a specific index range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/setconstantvalue(_:type:index:))*