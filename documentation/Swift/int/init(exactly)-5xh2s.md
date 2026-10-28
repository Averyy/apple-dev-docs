# init(exactly:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates an integer from the given floating-point value, if it can be represented exactly.

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
init?(exactly source: Float16)
```

## Discussion

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

### Converting with No Loss of Precision
- [init?<T>(exactly: T)](./init%28exactly%29-7yhn6.md)
- [init?(exactly: Double)](./init%28exactly%29-77kq8.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](./init%28exactly%29-7qdwf.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float80)](./init%28exactly%29-5kot1.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(exactly:)-5xh2s)*