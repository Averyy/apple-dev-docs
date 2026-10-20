# init(exactly:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new instance from the given value, if it can be represented exactly.

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
init?<Source>(exactly value: Source) where Source : BinaryFloatingPoint
```

#### Discussion

If the given floating-point value cannot be represented exactly, the result is `nil`.

## Parameters

- `value`: A floating-point value to be converted.

## See Also

### Converting with No Loss of Precision
- [init?(exactly: Double)](./init%28exactly%29-89na7.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float)](./init%28exactly%29-89pn7.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float80)](./init%28exactly%29-6l5fa.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: NSNumber)](./init%28exactly%29-zknq.md)
- [init?<Source>(exactly: Source)](./init%28exactly%29-1h1oe.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?(exactly: Float16)](./init%28exactly%29-8ho5q.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/init(exactly:)-8esr8)*