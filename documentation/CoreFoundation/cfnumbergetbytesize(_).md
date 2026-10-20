# CFNumberGetByteSize(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of bytes used by a CFNumber object to store its value.

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
func CFNumberGetByteSize(_ number: CFNumber!) -> CFIndex
```

```c
extern CFIndex CFNumberGetByteSize(CFNumberRef number);
```

#### Return Value

The size in bytes of the value contained in `number`.

#### Discussion

Because a CFNumber object might store a value using a type different from that of the original value with which it was created, this function may return a size different from the size of the original value’s type.

## Parameters

- `number`: The CFNumber object to examine.

## See Also

### Getting Information About Numbers
- [func CFNumberGetType(CFNumber!) -> CFNumberType](./cfnumbergettype%28_%29.md)
  Returns the type used by a CFNumber object to store its value.
- [func CFNumberGetValue(CFNumber!, CFNumberType, UnsafeMutableRawPointer!) -> Bool](./cfnumbergetvalue%28_,_,_%29.md)
  Obtains the value of a CFNumber object cast to a specified type.
- [func CFNumberIsFloatType(CFNumber!) -> Bool](./cfnumberisfloattype%28_%29.md)
  Determines whether a CFNumber object contains a value stored as one of the defined floating point types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumbergetbytesize(_:))*