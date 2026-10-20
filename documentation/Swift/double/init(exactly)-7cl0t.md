# init(exactly:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

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

If `other` can’t be represented as an instance of `Double` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float = 21.25
let y = Double(exactly: x)
// y == Optional.some(21.25)

let z = Double(exactly: Float.nan)
// z == nil
```

## Parameters

- `other`: The value to use for the new instance.

## See Also

### Converting with No Loss of Precision
- [init?<Source>(exactly: Source)](./init%28exactly%29-8esra.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init?<Source>(exactly: Source)](./init%28exactly%29-1h1oc.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?<Source>(exactly: Source)](./init%28exactly%29-2uexo.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?(exactly: Double)](./init%28exactly%29-2l6p1.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float16)](./init%28exactly%29-50ofc.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float80)](./init%28exactly%29-63925.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: NSNumber)](./init%28exactly%29-8e00y.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(exactly:)-7cl0t)*