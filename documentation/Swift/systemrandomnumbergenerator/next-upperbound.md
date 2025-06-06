# next(upperBound:)

**Framework**: Swift  
**Kind**: method

Returns a random value that is less than the given upper bound.

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
mutating func next<T>(upperBound: T) -> T where T : FixedWidthInteger, T : UnsignedInteger
```

#### Return Value

A random value of `T` in the range `0..<upperBound`. Every value in the range `0..<upperBound` is equally likely to be returned.

#### Discussion

Use this method when you need random binary data to generate another value. If you need an integer value within a specific range, use the static `random(in:using:)` method on that integer type instead of this method.

## Parameters

- `upperBound`: The upper bound for the randomly generated value.   Must be non-zero.

## See Also

- [func next() -> UInt64](systemrandomnumbergenerator/next.md)
  Returns a value from a uniform, independent distribution of binary data.
- [func next<T>() -> T](systemrandomnumbergenerator/next-2x0ly.md)
  Returns a value from a uniform, independent distribution of binary data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/systemrandomnumbergenerator/next(upperbound:))*