# Data.Deallocator.virtualMemory

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

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
case virtualMemory
```

## See Also

### Enumeration Cases
- [case custom((UnsafeMutableRawPointer, Int) -> Void)](./custom%28_%29.md)
  A custom deallocator.
- [Data.Deallocator.free](./free.md)
  Use `free`.
- [Data.Deallocator.none](./none.md)
  Do nothing upon deallocation.
- [Data.Deallocator.unmap](./unmap.md)
  Use `munmap`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/deallocator/virtualmemory)*