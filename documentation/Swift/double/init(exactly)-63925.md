# init(exactly:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new instance initialized to the given value, if it can be represented without rounding.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init?(exactly other: Float80)
```

#### Discussion

If `other` can’t be represented as an instance of `Double` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float80 = 21.25
let y = Double(exactly: x)
// y == Optional.some(21.25)

let z = Double(exactly: Float80.nan)
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
- [init?(exactly: Float)](./init%28exactly%29-7cl0t.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float16)](./init%28exactly%29-50ofc.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: NSNumber)](./init%28exactly%29-8e00y.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(exactly:)-63925)*