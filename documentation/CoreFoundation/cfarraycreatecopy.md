# CFArrayCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new immutable array with the values from another array.

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
func CFArrayCreateCopy(_ allocator: CFAllocator!, _ theArray: CFArray!) -> CFArray!
```

#### Return Value

A new CFArray object that contains the same values as `theArray`. Ownership follows [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The pointer values from `theArray` are copied into the new array; the values are also retained by the new array. The count of the new array is the same as `theArray`. The new array uses the same callbacks as `theArray`.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new array and its storage for values. Pass   or   to use the current default allocator.
- `theArray`: The array to copy.

## See Also

- [func CFArrayCreate(CFAllocator!, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex, UnsafePointer<CFArrayCallBacks>!) -> CFArray!](cfarraycreate(_:_:_:_:).md)
  Creates a new immutable array with the given values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraycreatecopy(_:_:))*