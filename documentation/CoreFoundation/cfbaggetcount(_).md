# CFBagGetCount(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of values currently in a bag.

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
func CFBagGetCount(_ theBag: CFBag!) -> CFIndex
```

```c
extern CFIndex CFBagGetCount(CFBagRef theBag);
```

#### Return Value

The number of values in `theBag`.

## Parameters

- `theBag`: The bag to examine.

## See Also

### Examining a Bag
- [func CFBagContainsValue(CFBag!, UnsafeRawPointer!) -> Bool](./cfbagcontainsvalue%28_,_%29.md)
  Reports whether or not a value is in a bag.
- [func CFBagGetCountOfValue(CFBag!, UnsafeRawPointer!) -> CFIndex](./cfbaggetcountofvalue%28_,_%29.md)
  Returns the number of times a value occurs in a bag.
- [func CFBagGetValue(CFBag!, UnsafeRawPointer!) -> UnsafeRawPointer!](./cfbaggetvalue%28_,_%29.md)
  Returns a requested value from a bag.
- [func CFBagGetValueIfPresent(CFBag!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfbaggetvalueifpresent%28_,_,_%29.md)
  Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [func CFBagGetValues(CFBag!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfbaggetvalues%28_,_%29.md)
  Fills a buffer with values from a bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbaggetcount(_:))*