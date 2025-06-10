# random(in:using:)

**Framework**: Swift  
**Kind**: method

Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.

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
static func random<T>(in range: Range<Self.Scalar>, using generator: inout T) -> Self where T : RandomNumberGenerator
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd4/random(in:using:)-7x9mr)*