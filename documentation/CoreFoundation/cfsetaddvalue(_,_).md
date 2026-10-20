# CFSetAddValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds a value to a CFMutableSet object.

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
func CFSetAddValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theSet`: The set to modify.
- `value`: A CFType object or a pointer value to add to `theSet` (or the value itself, if it fits into the size of a pointer). `value` is retained by `theSet` using the retain callback provided when `theSet` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined. If `value` already exists in the collection, this function returns without doing anything.

## See Also

- [func CFSetCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFSetCallBacks>!) -> CFMutableSet!](cfsetcreatemutable(_:_:_:).md)
  Creates an empty CFMutableSet object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetaddvalue(_:_:))*