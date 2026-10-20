# CFBagRemoveValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes a value from a mutable bag.

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
func CFBagRemoveValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

```c
extern void CFBagRemoveValue(CFMutableBagRef theBag, const void *value);
```

## Parameters

- `theBag`: The bag from which `value` is to be removed.
- `value`: The value to be removed from the collection.

## See Also

### Modifying a Mutable Bag
- [func CFBagAddValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagaddvalue%28_,_%29.md)
  Adds a value to a mutable bag.
- [func CFBagRemoveAllValues(CFMutableBag!)](./cfbagremoveallvalues%28_%29.md)
  Removes all values from a mutable bag.
- [func CFBagReplaceValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagreplacevalue%28_,_%29.md)
  Replaces a value in a mutable bag.
- [func CFBagSetValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagsetvalue%28_,_%29.md)
  Sets a value in a mutable bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagremovevalue(_:_:))*