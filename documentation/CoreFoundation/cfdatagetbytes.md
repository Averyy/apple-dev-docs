# CFDataGetBytes(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Copies the byte contents of a CFData object to an external buffer.

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
func CFDataGetBytes(_ theData: CFData!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UInt8>!)
```

## Parameters

- `theData`: The CFData object to examine.
- `range`: The range of bytes in   to get. To get all of the contents, pass  .
- `buffer`: A pointer to the byte buffer of length   that is allocated on the stack or heap. On return, the buffer contains the requested range of bytes.

## See Also

- [func CFDataGetBytePtr(CFData!) -> UnsafePointer<UInt8>!](cfdatagetbyteptr(_:).md)
  Returns a read-only pointer to the bytes of a CFData object.
- [func CFDataGetLength(CFData!) -> CFIndex](cfdatagetlength(_:).md)
  Returns the number of bytes contained by a CFData object.
- [func CFDataFind(CFData!, CFData!, CFRange, CFDataSearchFlags) -> CFRange](cfdatafind(_:_:_:_:).md)
  Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatagetbytes(_:_:_:))*