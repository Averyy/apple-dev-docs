# mappedIfSafe

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A hint indicating the file should be mapped into virtual memory, if possible and safe.

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
static var mappedIfSafe: NSData.ReadingOptions { get }
```

```c
NSDataReadingMappedIfSafe
```

## See Also

### Constants
- [static var uncached: NSData.ReadingOptions](./uncached.md)
  A hint indicating the file should not be stored in the file-system caches.
- [static var alwaysMapped: NSData.ReadingOptions](./alwaysmapped.md)
  Hint to map the file in if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/readingoptions/mappedifsafe)*