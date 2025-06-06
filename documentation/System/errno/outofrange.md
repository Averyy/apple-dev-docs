# outOfRange

**Framework**: System  
**Kind**: property

Numerical result out of range.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var outOfRange: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A numerical result of the function was too large to fit in the available space; for example, because it exceeded a floating point number’s level of precision.

The corresponding C error is `ERANGE`.

## See Also

- [static var outOfDomain: Errno](errno/outofdomain.md)
  Numerical argument out of domain.
- [static var overflow: Errno](errno/overflow.md)
  Value too large to be stored in data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/outofrange)*