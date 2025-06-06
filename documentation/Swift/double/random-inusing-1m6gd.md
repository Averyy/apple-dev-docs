# random(in:using:)

**Framework**: Swift  
**Kind**: method

Returns a random value within the specified range, using the given generator as a source for randomness.

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
static func random<T>(in range: Range<Self>, using generator: inout T) -> Self where T : RandomNumberGenerator
```

#### Return Value

A random value within the bounds of `range`.

#### Discussion

Use this method to generate a floating-point value within a specific range when you are using a custom random number generator. This example creates three new values in the range `10.0 ..< 20.0`.

```swift
for _ in 1...3 {
    print(Double.random(in: 10.0 ..< 20.0, using: &myGenerator))
}
// Prints "18.1900709259179"
// Prints "14.2286325689993"
// Prints "13.1485686260762"
```

The `random(in:using:)` static method chooses a random value from a continuous uniform distribution in `range`, and then converts that value to the nearest representable value in this type. Depending on the size and span of `range`, some concrete values may be represented more frequently than others.

> **Note**: The algorithm used to create random values may change in a future version of Swift. If you’re passing a generator that results in the same sequence of floating-point values each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

The algorithm used to create random values may change in a future version of Swift. If you’re passing a generator that results in the same sequence of floating-point values each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

## Parameters

- `range`: The range in which to create a random value.    must be finite and non-empty.
- `generator`: The random number generator to use when creating the   new random value.

## See Also

- [static func random(in: Range<Self>) -> Self](double/random(in:)-6idef.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](double/random(in:)-5o5ha.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](double/random(in:using:)-613hz.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/random(in:using:)-1m6gd)*