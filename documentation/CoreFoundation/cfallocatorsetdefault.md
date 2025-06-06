# CFAllocatorSetDefault(_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the given allocator as the default for the current thread.

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
func CFAllocatorSetDefault(_ allocator: CFAllocator!)
```

#### Discussion

The `CFAllocatorSetDefault` function sets the allocator that is used in the current thread whenever `NULL` is specified as an allocator argument. Generally, most allocations use the default allocator. Because of this, the default allocator must be prepared to deal with arbitrary memory-allocation requests. In addition, the size and number of requests can change between releases.

A further characteristic of the default allocator is that it can never be released, even if another allocator replaces it as the default. Not only is it impractical to release a default allocator (because there might be caches created somewhere that refer to the allocator) but it is generally safer and more efficient to keep it around.

If you wish to use a custom allocator in a context, the best approach is to specify it in the first parameter of creation functions rather than to set it as the default. Generally, setting the default allocator is not encouraged. If you do set an allocator as the default, either do it for the life time of your application or do it in a nested fashion (that is, restore the previous allocator before you exit your context). The latter approach might be more appropriate for plug-ins or libraries that wish to set the default allocator.

## Parameters

- `allocator`: The allocator to set as the default for the current thread.

## See Also

- [func CFAllocatorGetDefault() -> Unmanaged<CFAllocator>!](cfallocatorgetdefault().md)
  Gets the default allocator object for the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorsetdefault(_:))*