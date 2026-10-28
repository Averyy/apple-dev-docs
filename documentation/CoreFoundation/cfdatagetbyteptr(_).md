# CFDataGetBytePtr(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a read-only pointer to the bytes of a CFData object.

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
func CFDataGetBytePtr(_ theData: CFData!) -> UnsafePointer<UInt8>!
```

```c
extern const UInt8 *CFDataGetBytePtr(CFDataRef theData);
```

## Return Value

A read-only pointer to the bytes associated with `theData`.

## Discussion

This function is guaranteed to return a pointer to a CFData object’s internal bytes. CFData, unlike CFString, does not hide its internal storage.

## Parameters

- `theData`: The CFData object to examine.

## See Also

### Examining a CFData Object
- [func CFDataGetBytes(CFData!, CFRange, UnsafeMutablePointer<UInt8>!)](./cfdatagetbytes%28_,_,_%29.md)
  Copies the byte contents of a CFData object to an external buffer.
- [func CFDataGetLength(CFData!) -> CFIndex](./cfdatagetlength%28_%29.md)
  Returns the number of bytes contained by a CFData object.
- [func CFDataFind(CFData!, CFData!, CFRange, CFDataSearchFlags) -> CFRange](./cfdatafind%28_,_,_,_%29.md)
  Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatagetbyteptr(_:))*