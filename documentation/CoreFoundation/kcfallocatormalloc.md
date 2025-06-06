# kCFAllocatorMalloc

**Framework**: Core Foundation  
**Kind**: var

This allocator uses `malloc()`, `realloc()`, and `free()`.

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
let kCFAllocatorMalloc: CFAllocator!
```

#### Discussion

Typically you should not use this allocator, use `kCFAllocatorDefault` instead. This allocator is useful as the `bytesDeallocator` in CFData or `contentsDeallocator` in CFString where the memory was obtained as a result  of `malloc` type functions.

## See Also

- [let kCFAllocatorDefault: CFAllocator!](kcfallocatordefault.md)
  This is a synonym for `NULL`.
- [let kCFAllocatorSystemDefault: CFAllocator!](kcfallocatorsystemdefault.md)
  Default system allocator.
- [let kCFAllocatorMallocZone: CFAllocator!](kcfallocatormalloczone.md)
  This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.
- [let kCFAllocatorNull: CFAllocator!](kcfallocatornull.md)
  This allocator does nothing—it allocates no memory.
- [let kCFAllocatorUseContext: CFAllocator!](kcfallocatorusecontext.md)
  Special allocator argument to [`CFAllocatorCreate(_:_:)`](cfallocatorcreate(_:_:).md)—it uses the functions given in the context to allocate the allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfallocatormalloc)*