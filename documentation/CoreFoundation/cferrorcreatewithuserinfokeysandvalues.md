# CFErrorCreateWithUserInfoKeysAndValues(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new CFError object using given keys and values to create the user info dictionary.

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
func CFErrorCreateWithUserInfoKeysAndValues(_ allocator: CFAllocator!, _ domain: CFErrorDomain!, _ code: CFIndex, _ userInfoKeys: UnsafePointer<UnsafeRawPointer?>!, _ userInfoValues: UnsafePointer<UnsafeRawPointer?>!, _ numUserInfoValues: CFIndex) -> CFError!
```

#### Return Value

A new CFError object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `domain`: A CFString that identifies the error domain. If this reference is   or is otherwise not a valid CFString, the behavior is undefined.
- `code`: A CFIndex that identifies the error code. The code is interpreted within the context of the error domain.
- `userInfoKeys`: An array of   CFStrings used as keys in creating the userInfo dictionary. The value of this parameter can be   if   is  .
- `userInfoValues`: An array of   CF types used as values in creating the userInfo dictionary.  The value of this parameter can be   if   is  .
- `numUserInfoValues`: The number of keys and values in the   and   arrays.

## See Also

- [func CFErrorCreate(CFAllocator!, CFErrorDomain!, CFIndex, CFDictionary!) -> CFError!](cferrorcreate(_:_:_:_:).md)
  Creates a new CFError object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cferrorcreatewithuserinfokeysandvalues(_:_:_:_:_:_:))*