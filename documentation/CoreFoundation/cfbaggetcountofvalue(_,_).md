# CFBagGetCountOfValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of times a value occurs in a bag.

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
func CFBagGetCountOfValue(_ theBag: CFBag!, _ value: UnsafeRawPointer!) -> CFIndex
```

```c
extern CFIndex CFBagGetCountOfValue(CFBagRef theBag, const void *value);
```

#### Return Value

The number of times `value` occurs in `theBag`.

## Parameters

- `theBag`: The bag to examine.
- `value`: The value for which to find matches in `theBag`. The equal callback provided when `theBag` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theBag`, is not understood by the equal callback, the behavior is undefined.

## See Also

### Examining a Bag
- [func CFBagContainsValue(CFBag!, UnsafeRawPointer!) -> Bool](./cfbagcontainsvalue%28_,_%29.md)
  Reports whether or not a value is in a bag.
- [func CFBagGetCount(CFBag!) -> CFIndex](./cfbaggetcount%28_%29.md)
  Returns the number of values currently in a bag.
- [func CFBagGetValue(CFBag!, UnsafeRawPointer!) -> UnsafeRawPointer!](./cfbaggetvalue%28_,_%29.md)
  Returns a requested value from a bag.
- [func CFBagGetValueIfPresent(CFBag!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfbaggetvalueifpresent%28_,_,_%29.md)
  Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [func CFBagGetValues(CFBag!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfbaggetvalues%28_,_%29.md)
  Fills a buffer with values from a bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbaggetcountofvalue(_:_:))*