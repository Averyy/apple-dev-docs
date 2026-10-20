# CFSetAddValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Adds a value to a CFMutableSet object.

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
func CFSetAddValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!)
```

```c
extern void CFSetAddValue(CFMutableSetRef theSet, const void *value);
```

## Parameters

- `theSet`: The set to modify.
- `value`: A CFType object or a pointer value to add to `theSet` (or the value itself, if it fits into the size of a pointer).

  `value` is retained by `theSet` using the retain callback provided when `theSet` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined. If `value` already exists in the collection, this function returns without doing anything.

## See Also

### CFMutableSet Miscellaneous Functions
- [func CFSetCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFSetCallBacks>!) -> CFMutableSet!](./cfsetcreatemutable%28_,_,_%29.md)
  Creates an empty CFMutableSet object.
- [func CFSetCreateMutableCopy(CFAllocator!, CFIndex, CFSet!) -> CFMutableSet!](./cfsetcreatemutablecopy%28_,_,_%29.md)
  Creates a new mutable set with the values from another set.
- [func CFSetRemoveAllValues(CFMutableSet!)](./cfsetremoveallvalues%28_%29.md)
  Removes all values from a CFMutableSet object.
- [func CFSetRemoveValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetremovevalue%28_,_%29.md)
  Removes a value from a CFMutableSet object.
- [func CFSetReplaceValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetreplacevalue%28_,_%29.md)
  Replaces a value in a CFMutableSet object.
- [func CFSetSetValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetsetvalue%28_,_%29.md)
  Sets a value in a CFMutableSet object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetaddvalue(_:_:))*