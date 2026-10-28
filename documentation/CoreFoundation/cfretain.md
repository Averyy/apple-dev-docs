# CFRetain

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Retains a Core Foundation object.

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
extern CFTypeRefCFRetain(CFTypeRef cf);
```

## Return Value

The input value, `cf`.

## Discussion

You should retain a Core Foundation object when you receive it from elsewhere (that is, you did not create or copy it) and you want it to persist. If you retain a Core Foundation object you are responsible for releasing it (see [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)).

### Special Considerations

If `cf` is `NULL`, this will cause a runtime error and your application will crash.

## Parameters

- `cf`: The CFType object to retain. This value must not be `NULL`

## See Also

### Memory Management
- [func CFGetAllocator(CFTypeRef!) -> CFAllocator!](./cfgetallocator%28_%29.md)
  Returns the allocator used to allocate a Core Foundation object.
- [func CFGetRetainCount(CFTypeRef!) -> CFIndex](./cfgetretaincount%28_%29.md)
  Returns the reference count of a Core Foundation object.
- [CFMakeCollectable](./cfmakecollectable.md)
  Makes a newly-allocated Core Foundation object eligible for garbage collection.
- [CFRelease](./cfrelease.md)
  Releases a Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfretain)*