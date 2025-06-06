# init(exactly:)

**Framework**: Swift  
**Kind**: init

Creates a new instance initialized to the given value, if it can be represented without rounding.

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
init?(exactly other: Float)
```

#### Discussion

If `other` can’t be represented as an instance of `Float` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float = 21.25
let y = Float(exactly: x)
// y == Optional.some(21.25)

let z = Float(exactly: Float.nan)
// z == nil
```

## Parameters

- `other`: The value to use for the new instance.

## See Also

- [init?<Source>(exactly: Source)](float/init(exactly:)-8esr8.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init?(exactly: Double)](float/init(exactly:)-89na7.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float80)](float/init(exactly:)-6l5fa.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: NSNumber)](float/init(exactly:)-zknq.md)
- [init?<Source>(exactly: Source)](float/init(exactly:)-1h1oe.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?(exactly: Float16)](float/init(exactly:)-8ho5q.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/init(exactly:)-89pn7)*