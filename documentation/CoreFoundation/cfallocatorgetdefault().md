# CFAllocatorGetDefault()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Gets the default allocator object for the current thread.

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
func CFAllocatorGetDefault() -> Unmanaged<CFAllocator>!
```

```c
extern CFAllocatorRefCFAllocatorGetDefault();
```

## Return Value

A reference to the default allocator for the current thread. If none has been explicitly set, returns the generic system allocator, [`kCFAllocatorSystemDefault`](./kcfallocatorsystemdefault.md). Ownership follows [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

See the discussion for [`CFAllocatorSetDefault(_:)`](./cfallocatorsetdefault%28_%29.md) for more detail on the default allocator and for advice on how and when to set a custom allocator as the default.

## See Also

### Getting and Setting the Default Allocator
- [func CFAllocatorSetDefault(CFAllocator!)](./cfallocatorsetdefault%28_%29.md)
  Sets the given allocator as the default for the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorgetdefault())*