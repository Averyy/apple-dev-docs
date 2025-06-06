# Data.Deallocator.free

**Framework**: Foundation  
**Kind**: case

Use `free`.

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
case free
```

## See Also

- [case custom((UnsafeMutableRawPointer, Int) -> Void)](data/deallocator/custom(_:).md)
  A custom deallocator.
- [Data.Deallocator.none](data/deallocator/none.md)
  Do nothing upon deallocation.
- [Data.Deallocator.unmap](data/deallocator/unmap.md)
  Use `munmap`.
- [Data.Deallocator.virtualMemory](data/deallocator/virtualmemory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/deallocator/free)*