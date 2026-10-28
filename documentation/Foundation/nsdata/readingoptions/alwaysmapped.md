# alwaysMapped

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Hint to map the file in if possible.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var alwaysMapped: NSData.ReadingOptions { get }
```

```c
NSDataReadingMappedAlways
```

## Discussion

This takes precedence over [`mappedIfSafe`](./mappedifsafe.md) if both are given.

## See Also

### Constants
- [static var mappedIfSafe: NSData.ReadingOptions](./mappedifsafe.md)
  A hint indicating the file should be mapped into virtual memory, if possible and safe.
- [static var uncached: NSData.ReadingOptions](./uncached.md)
  A hint indicating the file should not be stored in the file-system caches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/readingoptions/alwaysmapped)*