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
static func random<T>(in range: ClosedRange<Self>, using generator: inout T) -> Self where T : RandomNumberGenerator
```

#### Return Value

A random value within the bounds of `range`.

#### Discussion

Use this method to generate an integer within a specific range when you are using a custom random number generator. This example creates three new values in the range `1...100`.

```swift
for _ in 1...3 {
    print(Int.random(in: 1...100, using: &myGenerator))
}
// Prints "7"
// Prints "44"
// Prints "21"
```

## Parameters

- `range`: The range in which to create a random value.
- `generator`: The random number generator to use when creating the   new random value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/random(in:using:)-535e1)*