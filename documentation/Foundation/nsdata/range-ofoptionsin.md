# range(of:options:in:)

**Framework**: Foundation  
**Kind**: method

Finds and returns the range of the first occurrence of the given data, within the given range, subject to given options.

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
func range(of dataToFind: Data, options mask: NSData.SearchOptions = [], in searchRange: NSRange) -> NSRange
```

#### Return Value

An [`NSRange`](nsrange-c.struct.md) structure giving the location and length of `dataToFind` within `searchRange`, modulo the options in `mask`. The range returned is relative to the start of the searched data, not the passed-in search range. Returns `{``NSNotFound``, 0}` if `dataToFind` is not found or is empty.

## Parameters

- `dataToFind`: The data for which to search.
- `mask`: A mask specifying search options. The   options may be specified singly or by combining them with the C bitwise   operator.
- `searchRange`: The range within the receiver in which to search for  . If this range is not within the data object’s range of bytes,   is raised.

## See Also

- [func subdata(with: NSRange) -> Data](nsdata/subdata(with:).md)
  Returns a new data object containing the data object’s bytes that fall within the limits specified by a given range.
- [NSData.SearchOptions](nsdata/searchoptions.md)
  Options for method used to search data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/range(of:options:in:))*