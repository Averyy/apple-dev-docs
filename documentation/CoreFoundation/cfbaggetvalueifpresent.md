# CFBagGetValueIfPresent(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Reports whether or not a value is in a bag, and returns that value indirectly if it exists.

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
func CFBagGetValueIfPresent(_ theBag: CFBag!, _ candidate: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool
```

#### Return Value

`true` if `value` is present in `theBag`, otherwise `false`.

#### Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the value returned in `value` may not have the same pointer equality as `candidate`.

## Parameters

- `theBag`: The bag to be searched.
- `candidate`: The value for which to find matches in  . The equal callback provided when   was created is used to compare. If the equal callback was  , pointer equality (in C, ==) is used. If  , or any other value in  , is not understood by the equal callback, the behavior is undefined.
- `value`: A pointer to a value object. Set to the matching value if it exists in the bag, otherwise  . If the value is a Core Foundation object, ownership follows the  .

## See Also

- [func CFBagContainsValue(CFBag!, UnsafeRawPointer!) -> Bool](cfbagcontainsvalue(_:_:).md)
  Reports whether or not a value is in a bag.
- [func CFBagGetCount(CFBag!) -> CFIndex](cfbaggetcount(_:).md)
  Returns the number of values currently in a bag.
- [func CFBagGetCountOfValue(CFBag!, UnsafeRawPointer!) -> CFIndex](cfbaggetcountofvalue(_:_:).md)
  Returns the number of times a value occurs in a bag.
- [func CFBagGetValue(CFBag!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfbaggetvalue(_:_:).md)
  Returns a requested value from a bag.
- [func CFBagGetValues(CFBag!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfbaggetvalues(_:_:).md)
  Fills a buffer with values from a bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbaggetvalueifpresent(_:_:_:))*