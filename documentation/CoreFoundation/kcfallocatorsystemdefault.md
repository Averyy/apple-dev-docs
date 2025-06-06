# kCFAllocatorSystemDefault

**Framework**: Core Foundation  
**Kind**: var

Default system allocator.

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
let kCFAllocatorSystemDefault: CFAllocator!
```

#### Discussion

You rarely need to use this.

## See Also

- [let kCFAllocatorDefault: CFAllocator!](kcfallocatordefault.md)
  This is a synonym for `NULL`.
- [let kCFAllocatorMalloc: CFAllocator!](kcfallocatormalloc.md)
  This allocator uses `malloc()`, `realloc()`, and `free()`.
- [let kCFAllocatorMallocZone: CFAllocator!](kcfallocatormalloczone.md)
  This allocator explicitly uses the default malloc zone, returned by `malloc_default_zone()`.
- [let kCFAllocatorNull: CFAllocator!](kcfallocatornull.md)
  This allocator does nothing—it allocates no memory.
- [let kCFAllocatorUseContext: CFAllocator!](kcfallocatorusecontext.md)
  Special allocator argument to [`CFAllocatorCreate(_:_:)`](cfallocatorcreate(_:_:).md)—it uses the functions given in the context to allocate the allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfallocatorsystemdefault)*