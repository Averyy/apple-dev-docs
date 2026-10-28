# CFBagAddValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Adds a value to a mutable bag.

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
func CFBagAddValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

```c
extern void CFBagAddValue(CFMutableBagRef theBag, const void *value);
```

## Discussion

The `value` parameter is retained by `theBag` using the retain callback provided when `theBag` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined. If `value` already exists in the collection, it is simply retained again—no memory is allocated for the added value. Use a CFSet object if you don’t want duplicate values in your collection.

## Parameters

- `theBag`: The bag to which `value` is added.
- `value`: A CFType object or a pointer value to add to `theBag` (or the value itself, if it fits into the size of a pointer).

## See Also

### Modifying a Mutable Bag
- [func CFBagRemoveAllValues(CFMutableBag!)](./cfbagremoveallvalues%28_%29.md)
  Removes all values from a mutable bag.
- [func CFBagRemoveValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagremovevalue%28_,_%29.md)
  Removes a value from a mutable bag.
- [func CFBagReplaceValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagreplacevalue%28_,_%29.md)
  Replaces a value in a mutable bag.
- [func CFBagSetValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagsetvalue%28_,_%29.md)
  Sets a value in a mutable bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagaddvalue(_:_:))*