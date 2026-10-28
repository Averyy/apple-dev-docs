# CFRelease

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Releases a Core Foundation object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
extern void CFRelease(CFTypeRef cf);
```

## Discussion

If the retain count of `cf` becomes zero the memory allocated to the object is deallocated and the object is destroyed. If you create, copy, or explicitly retain (see the [`CFRetain`](./cfretain.md) function) a Core Foundation object, you are responsible for releasing it when you no longer need it (see [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)).

### Special Considerations

If `cf` is `NULL`, this will cause a runtime error and your application will crash.

## Parameters

- `cf`: A CFType object to release. This value must not be `NULL`.

## See Also

### Memory Management
- [func CFGetAllocator(CFTypeRef!) -> CFAllocator!](./cfgetallocator%28_%29.md)
  Returns the allocator used to allocate a Core Foundation object.
- [func CFGetRetainCount(CFTypeRef!) -> CFIndex](./cfgetretaincount%28_%29.md)
  Returns the reference count of a Core Foundation object.
- [CFMakeCollectable](./cfmakecollectable.md)
  Makes a newly-allocated Core Foundation object eligible for garbage collection.
- [CFRetain](./cfretain.md)
  Retains a Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrelease)*