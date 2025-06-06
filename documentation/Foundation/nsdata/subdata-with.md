# subdata(with:)

**Framework**: Foundation  
**Kind**: method

Returns a new data object containing the data object’s bytes that fall within the limits specified by a given range.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func subdata(with range: NSRange) -> Data
```

#### Return Value

A data object containing the receiver’s bytes that fall within the limits specified by `range`.

#### Discussion

A sample using this method can be found in [`Working With Binary Data`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingBinaryData.html#//apple_ref/doc/uid/20000717).

## Parameters

- `range`: The range in the receiver from which to get the data. If this range is not within the data object’s range of bytes,   is raised.

## See Also

- [func range(of: Data, options: NSData.SearchOptions, in: NSRange) -> NSRange](nsdata/range(of:options:in:).md)
  Finds and returns the range of the first occurrence of the given data, within the given range, subject to given options.
- [NSData.SearchOptions](nsdata/searchoptions.md)
  Options for method used to search data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/subdata(with:))*