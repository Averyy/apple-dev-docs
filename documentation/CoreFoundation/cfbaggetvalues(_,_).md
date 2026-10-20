# CFBagGetValues(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Fills a buffer with values from a bag.

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
func CFBagGetValues(_ theBag: CFBag!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

```c
extern void CFBagGetValues(CFBagRef theBag, const void **values);
```

## Parameters

- `theBag`: The bag to examine.
- `values`: A C array of pointer-sized values to be filled with values from `theBag`. The value must be a valid C array of the appropriate type and size (that is, a size equal to the count of `theBag`).

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
- [func CFBagGetValueIfPresent(CFBag!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfbaggetvalueifpresent%28_,_,_%29.md)
  Reports whether or not a value is in a bag, and returns that value indirectly if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbaggetvalues(_:_:))*