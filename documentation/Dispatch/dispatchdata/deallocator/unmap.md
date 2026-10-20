# DispatchData.Deallocator.unmap

**Framework**: Dispatch  
**Kind**: case  
**Role**: Case

Use `munmap` to deallocate memory.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case unmap
```

## See Also

### Deallocators
- [DispatchData.Deallocator.free](./free.md)
  Use `free` to deallocate memory.
- [case custom(DispatchQueue?, () -> Void)](./custom%28_,_%29.md)
  Use a custom deallocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/deallocator/unmap)*