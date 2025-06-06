# CFBagAddValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds a value to a mutable bag.

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
func CFBagAddValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

#### Discussion

The `value` parameter is retained by `theBag` using the retain callback provided when `theBag` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined. If `value` already exists in the collection, it is simply retained again—no memory is allocated for the added value. Use a CFSet object if you don’t want duplicate values in your collection.

## Parameters

- `theBag`: The bag to which   is added.
- `value`: A CFType object or a pointer value to add to   (or the value itself, if it fits into the size of a pointer).

## See Also

- [func CFBagRemoveAllValues(CFMutableBag!)](cfbagremoveallvalues(_:).md)
  Removes all values from a mutable bag.
- [func CFBagRemoveValue(CFMutableBag!, UnsafeRawPointer!)](cfbagremovevalue(_:_:).md)
  Removes a value from a mutable bag.
- [func CFBagReplaceValue(CFMutableBag!, UnsafeRawPointer!)](cfbagreplacevalue(_:_:).md)
  Replaces a value in a mutable bag.
- [func CFBagSetValue(CFMutableBag!, UnsafeRawPointer!)](cfbagsetvalue(_:_:).md)
  Sets a value in a mutable bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagaddvalue(_:_:))*