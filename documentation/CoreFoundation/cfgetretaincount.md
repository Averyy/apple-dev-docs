# CFGetRetainCount(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the reference count of a Core Foundation object.

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
func CFGetRetainCount(_ cf: CFTypeRef!) -> CFIndex
```

#### Return Value

A number representing the reference count of `cf`.

#### Discussion

You increment the reference count using the [`CFRetain`](cfretain.md) function, and decrement the reference count using the [`CFRelease`](cfrelease.md) function.

This function may be useful for debugging memory leaks. You normally do not use this function, otherwise.

## Parameters

- `cf`: The CFType object to examine.

## See Also

- [func CFGetAllocator(CFTypeRef!) -> CFAllocator!](cfgetallocator(_:).md)
  Returns the allocator used to allocate a Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfgetretaincount(_:))*