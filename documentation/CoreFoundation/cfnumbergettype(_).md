# CFNumberGetType(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type used by a CFNumber object to store its value.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFNumberGetType(_ number: CFNumber!) -> CFNumberType
```

```c
extern CFNumberType CFNumberGetType(CFNumberRef number);
```

## Return Value

A constant that indicates the data type of the value contained in `number`. See [`CFNumberType`](./cfnumbertype.md) for a list of possible values.

## Discussion

The type specified in the call to [`CFNumberCreate(_:_:_:)`](./cfnumbercreate%28_,_,_%29.md) is not necessarily preserved when a new CFNumber object is created—it uses whatever internal storage type the creation function deems appropriate.

## Parameters

- `number`: The CFNumber object to examine.

## See Also

### Getting Information About Numbers
- [func CFNumberGetByteSize(CFNumber!) -> CFIndex](./cfnumbergetbytesize%28_%29.md)
  Returns the number of bytes used by a CFNumber object to store its value.
- [func CFNumberGetValue(CFNumber!, CFNumberType, UnsafeMutableRawPointer!) -> Bool](./cfnumbergetvalue%28_,_,_%29.md)
  Obtains the value of a CFNumber object cast to a specified type.
- [func CFNumberIsFloatType(CFNumber!) -> Bool](./cfnumberisfloattype%28_%29.md)
  Determines whether a CFNumber object contains a value stored as one of the defined floating point types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumbergettype(_:))*