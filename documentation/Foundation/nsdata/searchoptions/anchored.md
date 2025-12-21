# anchored

**Framework**: Foundation  
**Kind**: property

Search is limited to start (or end, if searching backwards) of the data object.

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
static var anchored: NSData.SearchOptions { get }
```

#### Discussion

This option performs searching only on bytes at the beginning of the range (or the end when using [`backwards`](nsdata/searchoptions/backwards.md)). No match at the beginning or end means nothing is found, even if a matching sequence of bytes occurs elsewhere in the data object.

## See Also

- [static var backwards: NSData.SearchOptions](nsdata/searchoptions/backwards.md)
  Search from the end of the data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/searchoptions/anchored)*