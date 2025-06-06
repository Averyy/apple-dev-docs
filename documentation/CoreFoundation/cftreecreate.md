# CFTreeCreate(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new CFTree object.

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
func CFTreeCreate(_ allocator: CFAllocator!, _ context: UnsafePointer<CFTreeContext>!) -> CFTree!
```

#### Return Value

A new CFTree object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new tree. Pass   or kCFAllocatorDefault to use the current default allocator.
- `context`: The   structure to be copied and used as the context of the new tree. The information pointer will be retained by the tree if a retain function is provided. If this value is not a valid C pointer to a   structure-sized block of storage, the result is undefined. If the version number of the storage is not a valid   version number, the result is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreecreate(_:_:))*