# kCFAllocatorMallocZone

**Framework**: Core Foundation  
**Kind**: var

This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.

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
let kCFAllocatorMallocZone: CFAllocator!
```

#### Discussion

You should only use this when an object is safe to be allocated in non-scanned memory.

## See Also

- [let kCFAllocatorDefault: CFAllocator!](kcfallocatordefault.md)
  This is a synonym for `NULL`.
- [let kCFAllocatorSystemDefault: CFAllocator!](kcfallocatorsystemdefault.md)
  Default system allocator.
- [let kCFAllocatorMalloc: CFAllocator!](kcfallocatormalloc.md)
  This allocator uses `malloc()`, `realloc()`, and `free()`.
- [let kCFAllocatorNull: CFAllocator!](kcfallocatornull.md)
  This allocator does nothing—it allocates no memory.
- [let kCFAllocatorUseContext: CFAllocator!](kcfallocatorusecontext.md)
  Special allocator argument to [`CFAllocatorCreate(_:_:)`](cfallocatorcreate(_:_:).md)—it uses the functions given in the context to allocate the allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfallocatormalloczone)*