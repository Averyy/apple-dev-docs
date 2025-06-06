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
static func random(in range: ClosedRange<Self>) -> Self
```

#### Return Value

A random value within the bounds of `range`.

#### Discussion

Use this method to generate an integer within a specific range. This example creates three new values in the range `1...100`.

```swift
for _ in 1...3 {
    print(Int.random(in: 1...100))
}
// Prints "53"
// Prints "64"
// Prints "5"
```

This method is equivalent to calling `random(in:using:)`, passing in the system’s default random generator.

## Parameters

- `range`: The range in which to create a random value.

## See Also

- [static func random(in: Range<Self>) -> Self](int/random(in:)-9mjpw.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](int/random(in:using:)-4lsb5.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](int/random(in:using:)-3dwv4.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/random(in:)-8zzqh)*