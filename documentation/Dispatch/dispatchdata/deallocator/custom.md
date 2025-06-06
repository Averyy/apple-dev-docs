# DispatchData.Deallocator.custom(_:_:)

**Framework**: Dispatch  
**Kind**: case

Use a custom deallocator.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@preconcurrency
case custom(DispatchQueue?, () -> Void)
```

## See Also

- [DispatchData.Deallocator.free](dispatchdata/deallocator/free.md)
  Use `free` to deallocate memory.
- [DispatchData.Deallocator.unmap](dispatchdata/deallocator/unmap.md)
  Use `munmap` to deallocate memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/deallocator/custom(_:_:))*