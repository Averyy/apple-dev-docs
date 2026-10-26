# CFMakeCollectable

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Makes a newly-allocated Core Foundation object eligible for garbage collection.

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
extern CFTypeRefCFMakeCollectable(CFTypeRef cf);
```

#### Return Value

`cf`.

#### Discussion

For more details, see Garbage Collection Programming Guide.

##### Special Considerations

If `cf` is `NULL`, this will cause a runtime error and your application will crash.

## Parameters

- `cf`: A CFType object to make collectable. This value must not be `NULL`.

## See Also

### Memory Management
- [func CFGetAllocator(CFTypeRef!) -> CFAllocator!](./cfgetallocator%28_%29.md)
  Returns the allocator used to allocate a Core Foundation object.
- [func CFGetRetainCount(CFTypeRef!) -> CFIndex](./cfgetretaincount%28_%29.md)
  Returns the reference count of a Core Foundation object.
- [CFRelease](./cfrelease.md)
  Releases a Core Foundation object.
- [CFRetain](./cfretain.md)
  Retains a Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmakecollectable)*