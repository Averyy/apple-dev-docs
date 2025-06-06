# setConstantValue(_:type:withName:)

**Framework**: Metal  
**Kind**: method

Sets a value for a function constant with a specific name.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setConstantValue(_ value: UnsafeRawPointer, type: MTLDataType, withName name: String)
```

#### Discussion

The first example declares a single function constant in a Metal Shading Language file.

```metal
constant bool a [[ function_constant(0) ]];
```

The next example sets that Boolean value by providing its specific name.

## Parameters

- `value`: A pointer to the constant value.
- `type`: The data type of the function constant.
- `name`: The name of the function constant.

## See Also

- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, index: Int)](mtlfunctionconstantvalues/setconstantvalue(_:type:index:).md)
  Sets a value for a function constant at a specific index.
- [func setConstantValues(UnsafeRawPointer, type: MTLDataType, range: Range<Int>)](mtlfunctionconstantvalues/setconstantvalues(_:type:range:).md)
  Sets values for a group of function constants within a specific index range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/setconstantvalue(_:type:withname:))*