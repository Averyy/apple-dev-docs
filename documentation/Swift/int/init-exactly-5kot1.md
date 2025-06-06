# init(exactly:)

**Framework**: Swift  
**Kind**: init

Creates an integer from the given floating-point value, if it can be represented exactly.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init?(exactly source: Float80)
```

#### Discussion

If the value passed as `source` is not representable exactly, the result is `nil`. In the following example, the constant `x` is successfully created from a value of `21.0`, while the attempt to initialize the constant `y` from `21.5` fails:

```swift
let x = Int(exactly: 21.0)
// x == Optional(21)
let y = Int(exactly: 21.5)
// y == nil
```

## Parameters

- `source`: A floating-point value to convert to an integer.

## See Also

- [init?<T>(exactly: T)](int/init(exactly:)-7yhn6.md)
- [init?(exactly: Double)](int/init(exactly:)-77kq8.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](int/init(exactly:)-7qdwf.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float16)](int/init(exactly:)-5xh2s.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(exactly:)-5kot1)*