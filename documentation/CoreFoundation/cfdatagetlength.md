# CFDataGetLength(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the number of bytes contained by a CFData object.

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
func CFDataGetLength(_ theData: CFData!) -> CFIndex
```

#### Return Value

An index that specifies the number of bytes in `theData`.

## Parameters

- `theData`: The CFData object to examine.

## See Also

- [func CFDataGetBytePtr(CFData!) -> UnsafePointer<UInt8>!](cfdatagetbyteptr(_:).md)
  Returns a read-only pointer to the bytes of a CFData object.
- [func CFDataGetBytes(CFData!, CFRange, UnsafeMutablePointer<UInt8>!)](cfdatagetbytes(_:_:_:).md)
  Copies the byte contents of a CFData object to an external buffer.
- [func CFDataFind(CFData!, CFData!, CFRange, CFDataSearchFlags) -> CFRange](cfdatafind(_:_:_:_:).md)
  Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatagetlength(_:))*