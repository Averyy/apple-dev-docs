# CFSetReplaceValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Replaces a value in a CFMutableSet object.

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
func CFSetReplaceValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!)
```

```c
extern void CFSetReplaceValue(CFMutableSetRef theSet, const void *value);
```

## Parameters

- `theSet`: The set to modify.
- `value`: The value to replace in `theSet`. If this value does not already exist in `theSet`, the function does nothing. You may pass the value itself instead of a pointer if it is pointer-size or less. The equal callback provided when `theSet` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theSet`, is not understood by the equal callback, the behavior is undefined.

## See Also

### CFMutableSet Miscellaneous Functions
- [func CFSetAddValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetaddvalue%28_,_%29.md)
  Adds a value to a CFMutableSet object.
- [func CFSetCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFSetCallBacks>!) -> CFMutableSet!](./cfsetcreatemutable%28_,_,_%29.md)
  Creates an empty CFMutableSet object.
- [func CFSetCreateMutableCopy(CFAllocator!, CFIndex, CFSet!) -> CFMutableSet!](./cfsetcreatemutablecopy%28_,_,_%29.md)
  Creates a new mutable set with the values from another set.
- [func CFSetRemoveAllValues(CFMutableSet!)](./cfsetremoveallvalues%28_%29.md)
  Removes all values from a CFMutableSet object.
- [func CFSetRemoveValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetremovevalue%28_,_%29.md)
  Removes a value from a CFMutableSet object.
- [func CFSetSetValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetsetvalue%28_,_%29.md)
  Sets a value in a CFMutableSet object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetreplacevalue(_:_:))*