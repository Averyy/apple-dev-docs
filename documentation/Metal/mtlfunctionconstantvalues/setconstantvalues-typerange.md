# setConstantValues(_:type:range:)

**Framework**: Metal  
**Kind**: method

Sets values for a group of function constants within a specific index range.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+

## Declaration

```swift
func setConstantValues(_ values: UnsafeRawPointer, type: MTLDataType, range: Range<Int>)
```

#### Discussion

Declare multiple function constants in Metal Shading Language (MSL).

```metal
constant bool a [[ function_constant(0) ]];
constant bool b [[ function_constant(1) ]];
constant bool c [[ function_constant(2) ]];
```

Set their values by assigning an index range of an array.

```swift
let abc = [true, true, true]
let constantValues = MTLFunctionConstantValues()
constantValues.setConstantValues(abc,
                                 type: .bool,
                                 with: NSMakeRange(0, 3))
```

## Parameters

- `values`: A pointer to the constant values.
- `type`: The data type of the function constants.
- `range`: The range of the function constant indices.

## See Also

- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, index: Int)](mtlfunctionconstantvalues/setconstantvalue(_:type:index:).md)
  Sets a value for a function constant at a specific index.
- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, withName: String)](mtlfunctionconstantvalues/setconstantvalue(_:type:withname:).md)
  Sets a value for a function constant with a specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/setconstantvalues(_:type:range:))*