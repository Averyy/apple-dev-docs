# uncached

**Framework**: Foundation  
**Kind**: property

A hint indicating the file should not be stored in the file-system caches.

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
static var uncached: NSData.ReadingOptions { get }
```

#### Discussion

For data being read once and discarded, this option can improve performance.

## See Also

- [static var mappedIfSafe: NSData.ReadingOptions](nsdata/readingoptions/mappedifsafe.md)
  A hint indicating the file should be mapped into virtual memory, if possible and safe.
- [static var alwaysMapped: NSData.ReadingOptions](nsdata/readingoptions/alwaysmapped.md)
  Hint to map the file in if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/readingoptions/uncached)*