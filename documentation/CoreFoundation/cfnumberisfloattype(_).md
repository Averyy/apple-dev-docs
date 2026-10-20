# CFNumberIsFloatType(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Determines whether a CFNumber object contains a value stored as one of the defined floating point types.

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
func CFNumberIsFloatType(_ number: CFNumber!) -> Bool
```

```c
extern Boolean CFNumberIsFloatType(CFNumberRef number);
```

#### Return Value

`true` if `number`’s value is one of the defined floating point types, otherwise `false`. The valid floating point types are listed in [`CFNumberType`](./cfnumbertype.md).

## Parameters

- `number`: The CFNumber object to examine.

## See Also

### Getting Information About Numbers
- [func CFNumberGetByteSize(CFNumber!) -> CFIndex](./cfnumbergetbytesize%28_%29.md)
  Returns the number of bytes used by a CFNumber object to store its value.
- [func CFNumberGetType(CFNumber!) -> CFNumberType](./cfnumbergettype%28_%29.md)
  Returns the type used by a CFNumber object to store its value.
- [func CFNumberGetValue(CFNumber!, CFNumberType, UnsafeMutableRawPointer!) -> Bool](./cfnumbergetvalue%28_,_,_%29.md)
  Obtains the value of a CFNumber object cast to a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberisfloattype(_:))*