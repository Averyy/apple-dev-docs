# random(in:)

**Framework**: Swift  
**Kind**: method

Returns a random value within the specified range.

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
static func random(in range: Range<Self>) -> Self
```

#### Return Value

A random value within the bounds of `range`.

#### Discussion

Use this method to generate a floating-point value within a specific range. This example creates three new values in the range `10.0 ..< 20.0`.

```swift
for _ in 1...3 {
    print(Double.random(in: 10.0 ..< 20.0))
}
// Prints "18.1900709259179"
// Prints "14.2286325689993"
// Prints "13.1485686260762"
```

The `random()` static method chooses a random value from a continuous uniform distribution in `range`, and then converts that value to the nearest representable value in this type. Depending on the size and span of `range`, some concrete values may be represented more frequently than others.

This method is equivalent to calling `random(in:using:)`, passing in the system’s default random generator.

## Parameters

- `range`: The range in which to create a random value.    must be finite and non-empty.

## See Also

- [static func random(in: ClosedRange<Self>) -> Self](binaryfloatingpoint/random(in:)-2j16p.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](binaryfloatingpoint/random(in:using:)-6pf7f.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](binaryfloatingpoint/random(in:using:)-2awm8.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryfloatingpoint/random(in:)-8jkjb)*