# CFSetCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable set containing the values of an existing set.

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
func CFSetCreateCopy(_ allocator: CFAllocator!, _ theSet: CFSet!) -> CFSet!
```

#### Return Value

A new set that contains the same values as `theSet`, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The pointer values from `theSet` are copied into the new set, and the values are retained by the new set. The count of the new set is the same as the count of `theSet`. The new set uses the same callbacks as `theSet`.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new set and its storage for values. Pass   or   to use the current default allocator.
- `theSet`: The set to copy.

## See Also

- [func CFSetCreate(CFAllocator!, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex, UnsafePointer<CFSetCallBacks>!) -> CFSet!](cfsetcreate(_:_:_:_:).md)
  Creates an immutable CFSet object containing supplied values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetcreatecopy(_:_:))*