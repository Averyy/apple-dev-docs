# CFBagCreateMutableCopy(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new mutable bag with the values from another bag.

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
func CFBagCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theBag: CFBag!) -> CFMutableBag!
```

#### Return Value

A new mutable bag that contains the same values as `theBag`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new bag and its storage for values. Pass   or kCFAllocatorDefault to use the current default allocator.
- `capacity`: The maximum number of values that can be contained by the new bag. The bag starts with the same count as  , and can grow to this number of values (and it can have less). If this value is  , the bag’s maximum capacity is not limited. This value must be greater than or equal to the count of  , and must not be negative.
- `theBag`: The bag to copy. The pointer values from   are copied into the new bag. However, the values are also retained by the new bag. The count of the new bag is the same as the count of  . The new bag uses the same callbacks as  .

## See Also

- [func CFBagCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFBagCallBacks>!) -> CFMutableBag!](cfbagcreatemutable(_:_:_:).md)
  Creates a new empty mutable bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagcreatemutablecopy(_:_:_:))*