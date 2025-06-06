# CFErrorCreate(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new CFError object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFErrorCreate(_ allocator: CFAllocator!, _ domain: CFErrorDomain!, _ code: CFIndex, _ userInfo: CFDictionary!) -> CFError!
```

#### Return Value

A new CFError object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `domain`: A CFString that identifies the error domain. If this reference is   or is otherwise not a valid CFString, the behavior is undefined.
- `code`: A CFIndex that identifies the error code. The code is interpreted within the context of the error domain.
- `userInfo`: A CFDictionary created with   and  . The dictionary is copied with  . If you do not want the userInfo dictionary, you can pass  , in which case an empty dictionary will be assigned.

## See Also

- [func CFErrorCreateWithUserInfoKeysAndValues(CFAllocator!, CFErrorDomain!, CFIndex, UnsafePointer<UnsafeRawPointer?>!, UnsafePointer<UnsafeRawPointer?>!, CFIndex) -> CFError!](cferrorcreatewithuserinfokeysandvalues(_:_:_:_:_:_:).md)
  Creates a new CFError object using given keys and values to create the user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cferrorcreate(_:_:_:_:))*