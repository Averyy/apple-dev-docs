# CFSetCreateMutable(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an empty CFMutableSet object.

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
func CFSetCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFSetCallBacks>!) -> CFMutableSet!
```

#### Return Value

A new mutable set, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new set and its storage for values. Pass `NULL` or [`kCFAllocatorDefault`](kcfallocatordefault.md) to use the current default allocator.
- `capacity`: The maximum number of values that can be contained by the new set. The set starts empty and can grow to this number of values (and it can have less). Pass `0` to specify that the maximum capacity is not limited. The value must not be negative.
- `callBacks`: A pointer to a [`CFSetCallBacks`](cfsetcallbacks.md) structure initialized with the callbacks to use to retain, release, describe, and compare values in the set. A copy of the contents of the callbacks structure is made, so that a pointer to a structure on the stack can be passed in or can be reused for multiple collection creations. This parameter may be `NULL`, which is treated as if a valid structure of version `0` with all fields `NULL` had been passed in. If any of the fields are not valid pointers to functions of the correct type, or this parameter is not a valid pointer to a `CFSetCallBacks` structure, the behavior is undefined. If any value put into the collection is not one understood by one of the callback functions, the behavior when that callback function is used is undefined. If the collection contains CFType objects only, then pass [`kCFTypeSetCallBacks`](kcftypesetcallbacks.md) as this parameter to use the default callback functions.

## See Also

- [func CFSetAddValue(CFMutableSet!, UnsafeRawPointer!)](cfsetaddvalue(_:_:).md)
  Adds a value to a CFMutableSet object.
- [func CFSetCreateMutableCopy(CFAllocator!, CFIndex, CFSet!) -> CFMutableSet!](cfsetcreatemutablecopy(_:_:_:).md)
  Creates a new mutable set with the values from another set.
- [func CFSetRemoveAllValues(CFMutableSet!)](cfsetremoveallvalues(_:).md)
  Removes all values from a CFMutableSet object.
- [func CFSetRemoveValue(CFMutableSet!, UnsafeRawPointer!)](cfsetremovevalue(_:_:).md)
  Removes a value from a CFMutableSet object.
- [func CFSetReplaceValue(CFMutableSet!, UnsafeRawPointer!)](cfsetreplacevalue(_:_:).md)
  Replaces a value in a CFMutableSet object.
- [func CFSetSetValue(CFMutableSet!, UnsafeRawPointer!)](cfsetsetvalue(_:_:).md)
  Sets a value in a CFMutableSet object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetcreatemutable(_:_:_:))*