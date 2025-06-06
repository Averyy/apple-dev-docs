# CFNumberGetValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Obtains the value of a CFNumber object cast to a specified type.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFNumberGetValue(_ number: CFNumber!, _ theType: CFNumberType, _ valuePtr: UnsafeMutableRawPointer!) -> Bool
```

#### Return Value

`true` if the operation was successful, otherwise `false`.

#### Discussion

If the argument type differs from the return type, and the conversion is lossy or the return value is out of range, then this function passes back an approximate value in `valuePtr` and returns `false`.

## Parameters

- `number`: The CFNumber object to examine.
- `theType`: A constant that specifies the data type to return. See   for a list of possible values.
- `valuePtr`: On return, contains the value of  .

## See Also

- [func CFNumberGetByteSize(CFNumber!) -> CFIndex](cfnumbergetbytesize(_:).md)
  Returns the number of bytes used by a CFNumber object to store its value.
- [func CFNumberGetType(CFNumber!) -> CFNumberType](cfnumbergettype(_:).md)
  Returns the type used by a CFNumber object to store its value.
- [func CFNumberIsFloatType(CFNumber!) -> Bool](cfnumberisfloattype(_:).md)
  Determines whether a CFNumber object contains a value stored as one of the defined floating point types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumbergetvalue(_:_:_:))*