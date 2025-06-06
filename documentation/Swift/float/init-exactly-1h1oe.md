# init(exactly:)

**Framework**: Swift  
**Kind**: init

Creates a new value, if the given integer can be represented exactly.

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
init?<Source>(exactly value: Source) where Source : BinaryInteger
```

#### Discussion

If the given integer cannot be represented exactly, the result is `nil`.

## Parameters

- `value`: The integer to convert to a floating-point value.

## See Also

- [init?<Source>(exactly: Source)](float/init(exactly:)-8esr8.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init?(exactly: Double)](float/init(exactly:)-89na7.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float)](float/init(exactly:)-89pn7.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float80)](float/init(exactly:)-6l5fa.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: NSNumber)](float/init(exactly:)-zknq.md)
- [init?(exactly: Float16)](float/init(exactly:)-8ho5q.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/init(exactly:)-1h1oe)*