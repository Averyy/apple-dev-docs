# kCFAllocatorNull

**Framework**: Core Foundation  
**Kind**: var

This allocator does nothing—it allocates no memory.

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
let kCFAllocatorNull: CFAllocator!
```

#### Discussion

This allocator is useful as the `bytesDeallocator` in CFData or `contentsDeallocator` in CFString where the memory should not be freed.

## See Also

- [let kCFAllocatorDefault: CFAllocator!](kcfallocatordefault.md)
  This is a synonym for `NULL`.
- [let kCFAllocatorSystemDefault: CFAllocator!](kcfallocatorsystemdefault.md)
  Default system allocator.
- [let kCFAllocatorMalloc: CFAllocator!](kcfallocatormalloc.md)
  This allocator uses `malloc()`, `realloc()`, and `free()`.
- [let kCFAllocatorMallocZone: CFAllocator!](kcfallocatormalloczone.md)
  This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.
- [let kCFAllocatorUseContext: CFAllocator!](kcfallocatorusecontext.md)
  Special allocator argument to [`CFAllocatorCreate(_:_:)`](cfallocatorcreate(_:_:).md)—it uses the functions given in the context to allocate the allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfallocatornull)*