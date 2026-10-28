# CFCharacterSetCreateMutable(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new empty mutable character set.

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
func CFCharacterSetCreateMutable(_ alloc: CFAllocator!) -> CFMutableCharacterSet!
```

```c
extern CFMutableCharacterSetRefCFCharacterSetCreateMutable(CFAllocatorRef alloc);
```

## Return Value

A new empty mutable character set. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

## See Also

### Creating a Mutable Character Set
- [func CFCharacterSetCreateMutableCopy(CFAllocator!, CFCharacterSet!) -> CFMutableCharacterSet!](./cfcharactersetcreatemutablecopy%28_,_%29.md)
  Creates a new mutable character set with the values from another character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatemutable(_:))*