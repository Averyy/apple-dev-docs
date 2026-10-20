# CFGetAllocator(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the allocator used to allocate a Core Foundation object.

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
func CFGetAllocator(_ cf: CFTypeRef!) -> CFAllocator!
```

#### Return Value

The allocator used to allocate memory for `cf`.

#### Discussion

When you are creating a Core Foundation object sometimes you want to ensure that the block of memory allocated for the object is from the same allocator used for another object. One way to do this is to reuse the allocator assigned to an existing Core Foundation object when you call a “creation” function.

## Parameters

- `cf`: The CFType object to examine.

## See Also

- [func CFGetRetainCount(CFTypeRef!) -> CFIndex](cfgetretaincount(_:).md)
  Returns the reference count of a Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfgetallocator(_:))*