# CFSetSetValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets a value in a CFMutableSet object.

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
func CFSetSetValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!)
```

```c
extern void CFSetSetValue(CFMutableSetRef theSet, const void *value);
```

#### Discussion

Depending on the implementation of the equal callback specified when creating `theSet`, the value that is replaced by `value` may not have the same pointer equality.

## Parameters

- `theSet`: The set to modify.
- `value`: The value to be set in `theSet`. If this value already exists in `theSet`, it is replaced. You may pass the value itself instead of a pointer to it if the value is pointer-size or less. If `theSet` is fixed-size and setting the value would increase its size beyond its capacity, the behavior is undefined.

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
- [func CFSetReplaceValue(CFMutableSet!, UnsafeRawPointer!)](./cfsetreplacevalue%28_,_%29.md)
  Replaces a value in a CFMutableSet object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetsetvalue(_:_:))*