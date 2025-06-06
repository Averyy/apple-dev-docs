# CFBagReplaceValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Replaces a value in a mutable bag.

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
func CFBagReplaceValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

#### Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the object that is replaced by `value` may not have the same pointer equality.

## Parameters

- `theBag`: The bag from which   is to be replaced.
- `value`: The value to be replaced in the collection. If this value does not already exist in the collection, the function does nothing. You may pass the value itself instead of a pointer if it is pointer-size or less. The equal callback provided when   was created is used to compare. If the equal callback was  , pointer equality (in C, ==) is used. If  , or any other value in  , is not understood by the equal callback, the behavior is undefined.

## See Also

- [func CFBagAddValue(CFMutableBag!, UnsafeRawPointer!)](cfbagaddvalue(_:_:).md)
  Adds a value to a mutable bag.
- [func CFBagRemoveAllValues(CFMutableBag!)](cfbagremoveallvalues(_:).md)
  Removes all values from a mutable bag.
- [func CFBagRemoveValue(CFMutableBag!, UnsafeRawPointer!)](cfbagremovevalue(_:_:).md)
  Removes a value from a mutable bag.
- [func CFBagSetValue(CFMutableBag!, UnsafeRawPointer!)](cfbagsetvalue(_:_:).md)
  Sets a value in a mutable bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagreplacevalue(_:_:))*