# CFDataFind(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFDataFind(_ theData: CFData!, _ dataToFind: CFData!, _ searchRange: CFRange, _ compareOptions: CFDataSearchFlags) -> CFRange
```

#### Return Value

The range representing the location and length of `dataToFind` within `searchRange`, modulo the options in `compareOptions`. The range returned is relative to the start of the searched data, not the passed-in search range. Returns [`kCFNotFound`](kcfnotfound.md) if `dataToFind` is not found.

## Parameters

- `theData`: The data object within which to search.
- `dataToFind`: The data to find. Must not be  .
- `searchRange`: The range within   to be searched.
- `compareOptions`: A bit mask specifying search options. The   options can be specified singly or combined with the C bitwise   operator

## See Also

- [func CFDataGetBytePtr(CFData!) -> UnsafePointer<UInt8>!](cfdatagetbyteptr(_:).md)
  Returns a read-only pointer to the bytes of a CFData object.
- [func CFDataGetBytes(CFData!, CFRange, UnsafeMutablePointer<UInt8>!)](cfdatagetbytes(_:_:_:).md)
  Copies the byte contents of a CFData object to an external buffer.
- [func CFDataGetLength(CFData!) -> CFIndex](cfdatagetlength(_:).md)
  Returns the number of bytes contained by a CFData object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatafind(_:_:_:_:))*