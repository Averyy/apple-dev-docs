# init(uncheckedBounds:)

**Framework**: Swift  
**Kind**: init

Creates an instance with the given bounds.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(uncheckedBounds bounds: (lower: Bound, upper: Bound))
```

#### Discussion

Because this initializer does not perform any checks, it should be used as an optimization only when you are absolutely certain that `lower` is less than or equal to `upper`. Using the closed range operator (`...`) to form `ClosedRange` instances is preferred.

## Parameters

- `bounds`: A tuple of the lower and upper bounds of the range.

## See Also

- [var hashValue: Int](closedrange/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/init(uncheckedbounds:))*