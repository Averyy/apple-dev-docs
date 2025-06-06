# CFBagGetValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a requested value from a bag.

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
func CFBagGetValue(_ theBag: CFBag!, _ value: UnsafeRawPointer!) -> UnsafeRawPointer!
```

#### Return Value

A pointer to `value`, or `NULL` if `value` is not in `theBag`. If the value is a Core Foundation object, ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the value returned may not have the same pointer equality as `value`.

## Parameters

- `theBag`: The bag to examine.
- `value`: The value for which to find matches in  . The equal callback provided when   was created is used to compare. If the equal callback was  , pointer equality (in C, ==) is used. If  , or any other value in  , is not understood by the equal callback, the behavior is undefined.

## See Also

- [func CFBagContainsValue(CFBag!, UnsafeRawPointer!) -> Bool](cfbagcontainsvalue(_:_:).md)
  Reports whether or not a value is in a bag.
- [func CFBagGetCount(CFBag!) -> CFIndex](cfbaggetcount(_:).md)
  Returns the number of values currently in a bag.
- [func CFBagGetCountOfValue(CFBag!, UnsafeRawPointer!) -> CFIndex](cfbaggetcountofvalue(_:_:).md)
  Returns the number of times a value occurs in a bag.
- [func CFBagGetValueIfPresent(CFBag!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfbaggetvalueifpresent(_:_:_:).md)
  Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [func CFBagGetValues(CFBag!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfbaggetvalues(_:_:).md)
  Fills a buffer with values from a bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbaggetvalue(_:_:))*