# outOfDomain

**Framework**: System  
**Kind**: property

Numerical argument out of domain.

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
static var outOfDomain: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A numerical input argument was outside the defined domain of the mathematical function.

The corresponding C error is `EDOM`.

## See Also

- [static var outOfRange: Errno](errno/outofrange.md)
  Numerical result out of range.
- [static var overflow: Errno](errno/overflow.md)
  Value too large to be stored in data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/outofdomain)*