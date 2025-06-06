# CFBagCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable bag with the values of another bag.

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
func CFBagCreateCopy(_ allocator: CFAllocator!, _ theBag: CFBag!) -> CFBag!
```

#### Return Value

A new bag that contains the same values as `theBag`, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new bag and its storage for values. Pass   or kCFAllocatorDefault to use the current default allocator.
- `theBag`: The bag to copy. The pointer values from   are copied into the new bag. However, the values are also retained by the new bag. The count of the new bag is the same as the count of  . The new bag uses the same callbacks as  .

## See Also

- [func CFBagCreate(CFAllocator!, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex, UnsafePointer<CFBagCallBacks>!) -> CFBag!](cfbagcreate(_:_:_:_:).md)
  Creates an immutable bag containing specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagcreatecopy(_:_:))*