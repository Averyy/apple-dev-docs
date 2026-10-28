# CFDataGetLength(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of bytes contained by a CFData object.

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
func CFDataGetLength(_ theData: CFData!) -> CFIndex
```

```c
extern CFIndex CFDataGetLength(CFDataRef theData);
```

## Return Value

An index that specifies the number of bytes in `theData`.

## Parameters

- `theData`: The CFData object to examine.

## See Also

### Examining a CFData Object
- [func CFDataGetBytePtr(CFData!) -> UnsafePointer<UInt8>!](./cfdatagetbyteptr%28_%29.md)
  Returns a read-only pointer to the bytes of a CFData object.
- [func CFDataGetBytes(CFData!, CFRange, UnsafeMutablePointer<UInt8>!)](./cfdatagetbytes%28_,_,_%29.md)
  Copies the byte contents of a CFData object to an external buffer.
- [func CFDataFind(CFData!, CFData!, CFRange, CFDataSearchFlags) -> CFRange](./cfdatafind%28_,_,_,_%29.md)
  Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatagetlength(_:))*