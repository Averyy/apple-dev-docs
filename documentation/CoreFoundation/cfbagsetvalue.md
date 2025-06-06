# CFBagSetValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets a value in a mutable bag.

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
func CFBagSetValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

#### Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the value that is replaced by `value` may not have the same pointer equality.

## Parameters

- `theBag`: The bag in which   is to be set.
- `value`: The value to be set in the collection. If this value already exists in  , it is replaced. You may pass the value itself instead of a pointer to it if the value is pointer-size or less. If   is fixed-size and the value is beyond its capacity, the behavior is undefined.

## See Also

- [func CFBagAddValue(CFMutableBag!, UnsafeRawPointer!)](cfbagaddvalue(_:_:).md)
  Adds a value to a mutable bag.
- [func CFBagRemoveAllValues(CFMutableBag!)](cfbagremoveallvalues(_:).md)
  Removes all values from a mutable bag.
- [func CFBagRemoveValue(CFMutableBag!, UnsafeRawPointer!)](cfbagremovevalue(_:_:).md)
  Removes a value from a mutable bag.
- [func CFBagReplaceValue(CFMutableBag!, UnsafeRawPointer!)](cfbagreplacevalue(_:_:).md)
  Replaces a value in a mutable bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagsetvalue(_:_:))*