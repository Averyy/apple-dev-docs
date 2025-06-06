# CFSetSetValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets a value in a CFMutableSet object.

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
func CFSetSetValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!)
```

#### Discussion

Depending on the implementation of the equal callback specified when creating `theSet`, the value that is replaced by `value` may not have the same pointer equality.

## Parameters

- `theSet`: The set to modify.
- `value`: The value to be set in  . If this value already exists in  , it is replaced. You may pass the value itself instead of a pointer to it if the value is pointer-size or less. If   is fixed-size and setting the value would increase its size beyond its capacity, the behavior is undefined.

## See Also

- [func CFSetAddValue(CFMutableSet!, UnsafeRawPointer!)](cfsetaddvalue(_:_:).md)
  Adds a value to a CFMutableSet object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetsetvalue(_:_:))*