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

- [init?<Source>(exactly: Source)](double/init(exactly:)-8esra.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init?<Source>(exactly: Source)](double/init(exactly:)-2uexo.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?(exactly: Double)](double/init(exactly:)-2l6p1.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float)](double/init(exactly:)-7cl0t.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float16)](double/init(exactly:)-50ofc.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float80)](double/init(exactly:)-63925.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: NSNumber)](double/init(exactly:)-8e00y.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(exactly:)-1h1oc)*