# CFBagReplaceValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Replaces a value in a mutable bag.

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
func CFBagReplaceValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

```c
extern void CFBagReplaceValue(CFMutableBagRef theBag, const void *value);
```

#### Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the object that is replaced by `value` may not have the same pointer equality.

## Parameters

- `theBag`: The bag from which `value` is to be replaced.
- `value`: The value to be replaced in the collection. If this value does not already exist in the collection, the function does nothing. You may pass the value itself instead of a pointer if it is pointer-size or less. The equal callback provided when `theBag` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theBag`, is not understood by the equal callback, the behavior is undefined.

## See Also

### Modifying a Mutable Bag
- [func CFBagAddValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagaddvalue%28_,_%29.md)
  Adds a value to a mutable bag.
- [func CFBagRemoveAllValues(CFMutableBag!)](./cfbagremoveallvalues%28_%29.md)
  Removes all values from a mutable bag.
- [func CFBagRemoveValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagremovevalue%28_,_%29.md)
  Removes a value from a mutable bag.
- [func CFBagSetValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagsetvalue%28_,_%29.md)
  Sets a value in a mutable bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagreplacevalue(_:_:))*