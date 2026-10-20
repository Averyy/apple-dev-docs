# uncached

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```c
NSDataReadingUncached
```

#### Discussion

For data being read once and discarded, this option can improve performance.

## See Also

### Constants
- [static var mappedIfSafe: NSData.ReadingOptions](./mappedifsafe.md)
  A hint indicating the file should be mapped into virtual memory, if possible and safe.
- [static var alwaysMapped: NSData.ReadingOptions](./alwaysmapped.md)
  Hint to map the file in if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/readingoptions/uncached)*