# CFBagContainsValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Reports whether or not a value is in a bag.

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
func CFBagContainsValue(_ theBag: CFBag!, _ value: UnsafeRawPointer!) -> Bool
```

#### Return Value

`true` if `value` is contained in `theBag`, otherwise `false`.

## Parameters

- `theBag`: The bag to examine.
- `value`: The value to match in  . The equal callback provided when   was created is used to compare. If the equal callback was  , pointer equality (in C, ==) is used. If  , or any other value in  , is not understood by the equal callback, the behavior is undefined.

## See Also

- [func CFBagGetCount(CFBag!) -> CFIndex](cfbaggetcount(_:).md)
  Returns the number of values currently in a bag.
- [func CFBagGetCountOfValue(CFBag!, UnsafeRawPointer!) -> CFIndex](cfbaggetcountofvalue(_:_:).md)
  Returns the number of times a value occurs in a bag.
- [func CFBagGetValue(CFBag!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfbaggetvalue(_:_:).md)
  Returns a requested value from a bag.
- [func CFBagGetValueIfPresent(CFBag!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfbaggetvalueifpresent(_:_:_:).md)
  Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [func CFBagGetValues(CFBag!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfbaggetvalues(_:_:).md)
  Fills a buffer with values from a bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagcontainsvalue(_:_:))*