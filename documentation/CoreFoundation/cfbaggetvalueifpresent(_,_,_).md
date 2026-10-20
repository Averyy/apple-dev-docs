# CFBagGetValueIfPresent(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Reports whether or not a value is in a bag, and returns that value indirectly if it exists.

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
func CFBagGetValueIfPresent(_ theBag: CFBag!, _ candidate: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool
```

```c
extern Boolean CFBagGetValueIfPresent(CFBagRef theBag, const void *candidate, const void **value);
```

#### Return Value

`true` if `value` is present in `theBag`, otherwise `false`.

#### Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the value returned in `value` may not have the same pointer equality as `candidate`.

## Parameters

- `theBag`: The bag to be searched.
- `candidate`: The value for which to find matches in `theBag`. The equal callback provided when `theBag` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `candidate`, or any other value in `theBag`, is not understood by the equal callback, the behavior is undefined.
- `value`: A pointer to a value object. Set to the matching value if it exists in the bag, otherwise `NULL`. If the value is a Core Foundation object, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining a Bag
- [func CFBagContainsValue(CFBag!, UnsafeRawPointer!) -> Bool](./cfbagcontainsvalue%28_,_%29.md)
  Reports whether or not a value is in a bag.
- [func CFBagGetCount(CFBag!) -> CFIndex](./cfbaggetcount%28_%29.md)
  Returns the number of values currently in a bag.
- [func CFBagGetCountOfValue(CFBag!, UnsafeRawPointer!) -> CFIndex](./cfbaggetcountofvalue%28_,_%29.md)
  Returns the number of times a value occurs in a bag.
- [func CFBagGetValue(CFBag!, UnsafeRawPointer!) -> UnsafeRawPointer!](./cfbaggetvalue%28_,_%29.md)
  Returns a requested value from a bag.
- [func CFBagGetValues(CFBag!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfbaggetvalues%28_,_%29.md)
  Fills a buffer with values from a bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbaggetvalueifpresent(_:_:_:))*