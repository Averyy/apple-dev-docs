# Data.Deallocator.custom(_:)

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A custom deallocator.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case custom((UnsafeMutableRawPointer, Int) -> Void)
```

## See Also

### Enumeration Cases
- [Data.Deallocator.free](./free.md)
  Use `free`.
- [Data.Deallocator.none](./none.md)
  Do nothing upon deallocation.
- [Data.Deallocator.unmap](./unmap.md)
  Use `munmap`.
- [Data.Deallocator.virtualMemory](./virtualmemory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/deallocator/custom(_:))*