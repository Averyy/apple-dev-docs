# ..<(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a half-open range that contains its lower bound but not its upper bound.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func ..< (minimum: Self, maximum: Self) -> Range<Self>
```

#### Discussion

Use the half-open range operator (`..<`) to create a range of any type that conforms to the `Comparable` protocol. This example creates a `Range<Double>` from zero up to, but not including, 5.0.

```swift
let lessThanFive = 0.0..<5.0
print(lessThanFive.contains(3.14))  // Prints "true"
print(lessThanFive.contains(5.0))   // Prints "false"
```

> **Note**: `minimum <= maximum`.

## Parameters

- `minimum`: The lower bound for the range.
- `maximum`: The upper bound for the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/'.._(_:_:))*