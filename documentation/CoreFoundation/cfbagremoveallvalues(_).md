# CFBagRemoveAllValues(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes all values from a mutable bag.

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
func CFBagRemoveAllValues(_ theBag: CFMutableBag!)
```

```c
extern void CFBagRemoveAllValues(CFMutableBagRef theBag);
```

## Parameters

- `theBag`: The bag from which all of the values are to be removed.

## See Also

### Modifying a Mutable Bag
- [func CFBagAddValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagaddvalue%28_,_%29.md)
  Adds a value to a mutable bag.
- [func CFBagRemoveValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagremovevalue%28_,_%29.md)
  Removes a value from a mutable bag.
- [func CFBagReplaceValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagreplacevalue%28_,_%29.md)
  Replaces a value in a mutable bag.
- [func CFBagSetValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagsetvalue%28_,_%29.md)
  Sets a value in a mutable bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagremoveallvalues(_:))*