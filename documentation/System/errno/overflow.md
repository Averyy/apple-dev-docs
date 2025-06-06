# overflow

**Framework**: System  
**Kind**: property

Value too large to be stored in data type.

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
static var overflow: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A numerical result of the function is too large to be stored in the space that the caller provided.

The corresponding C error is `EOVERFLOW`.

## See Also

- [static var outOfDomain: Errno](errno/outofdomain.md)
  Numerical argument out of domain.
- [static var outOfRange: Errno](errno/outofrange.md)
  Numerical result out of range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/overflow)*