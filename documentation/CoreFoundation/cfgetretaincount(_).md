# CFGetRetainCount(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the reference count of a Core Foundation object.

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
func CFGetRetainCount(_ cf: CFTypeRef!) -> CFIndex
```

```c
extern CFIndex CFGetRetainCount(CFTypeRef cf);
```

#### Return Value

A number representing the reference count of `cf`.

#### Discussion

You increment the reference count using the [`CFRetain`](./cfretain.md) function, and decrement the reference count using the [`CFRelease`](./cfrelease.md) function.

This function may be useful for debugging memory leaks. You normally do not use this function, otherwise.

## Parameters

- `cf`: The CFType object to examine.

## See Also

### Memory Management
- [func CFGetAllocator(CFTypeRef!) -> CFAllocator!](./cfgetallocator%28_%29.md)
  Returns the allocator used to allocate a Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfgetretaincount(_:))*