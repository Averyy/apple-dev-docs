# CFSetCreateMutableCopy(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new mutable set with the values from another set.

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
func CFSetCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theSet: CFSet!) -> CFMutableSet!
```

```c
extern CFMutableSetRefCFSetCreateMutableCopy(CFAllocatorRef allocator, CFIndex capacity, CFSetRef theSet);
```

#### Return Value

A new mutable set that contains the same values as `theSet`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new set and its storage for values. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `capacity`: The maximum number of values that can be contained by the new set. The set starts with the same number of values as `theSet` and can grow to this number of values (and it can have less).

  Pass `0` to specify that the maximum capacity is not limited. If non-`0`, `capacity` must be greater than or equal to the count of `theSet`.
- `theSet`: The set to copy. The pointer values from `theSet` are copied into the new set. The values are also retained by the new set. The count of the new set is the same as the count of `theSet`. The new set uses the same callbacks as `theSet`.

## See Also

### CFMutableSet Miscellaneous Functions
- [func CFSetAddValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetaddvalue%28_,_%29.md)
  Adds a value to a CFMutableSet object.
- [func CFSetCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFSetCallBacks>!) -> CFMutableSet!](./cfsetcreatemutable%28_,_,_%29.md)
  Creates an empty CFMutableSet object.
- [func CFSetRemoveAllValues(CFMutableSet!)](./cfsetremoveallvalues%28_%29.md)
  Removes all values from a CFMutableSet object.
- [func CFSetRemoveValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetremovevalue%28_,_%29.md)
  Removes a value from a CFMutableSet object.
- [func CFSetReplaceValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetreplacevalue%28_,_%29.md)
  Replaces a value in a CFMutableSet object.
- [func CFSetSetValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetsetvalue%28_,_%29.md)
  Sets a value in a CFMutableSet object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetcreatemutablecopy(_:_:_:))*