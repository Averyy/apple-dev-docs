# ABSearchConjunction

**Framework**: Address Book  
**Kind**: typealias  
**Role**: Type Alias

Constants used to create compound search elements.

**Availability**:
- macOS

## Declaration

```swift
typealias ABSearchConjunction = CFIndex
```

```c
typedef CFIndex ABSearchConjunction;
```

#### Discussion

These constants are used to create compound search elementswith the [`ABSearchElementCreateWithConjunction(_:_:)`](./absearchelementcreatewithconjunction%28_,_%29.md) function.

## Topics

### Constants
- [var kABSearchAnd: _ABSearchConjunction](./kabsearchand.md)
  Join the search elements together with theAND operand.
- [var kABSearchOr: _ABSearchConjunction](./kabsearchor.md)
  Join the search elements together with theOR operand.

## See Also

### Constants
- [typealias ABSearchComparison](./absearchcomparison.md)
  Constants used to specify the type of comparison beingmade.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/absearchconjunction)*