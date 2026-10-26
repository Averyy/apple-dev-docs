# setConstantValues:type:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets values for a group of function constants within a specific index range.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setConstantValues:(const void *) values type:(MTLDataType) type withRange:(NSRange) range;
```

#### Discussion

Declare multiple function constants in Metal Shading Language (MSL).

```metal
constant bool a [[ function_constant(0) ]];
constant bool b [[ function_constant(1) ]];
constant bool c [[ function_constant(2) ]];
```

Set their values by assigning an index range of an array.

```objective-c
const bool abc[3] = { true, true, true };
MTLFunctionConstantValues* constantValues = [MTLFunctionConstantValues new];
[constantValues setConstantValues:&abc
                             type:MTLDataTypeBool
                        withRange:NSMakeRange(0, 3)];
```

## Parameters

- `values`: A pointer to the constant values.
- `type`: The data type of the function constants.
- `range`: The range of the function constant indices.

## See Also

### Setting constant values
- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, index: Int)](./setconstantvalue%28_,type,index%29.md)
  Sets a value for a function constant at a specific index.
- [func setConstantValue(UnsafeRawPointer, type: MTLDataType, withName: String)](./setconstantvalue%28_,type,withname%29.md)
  Sets a value for a function constant with a specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/setconstantvalues:type:withrange:)*