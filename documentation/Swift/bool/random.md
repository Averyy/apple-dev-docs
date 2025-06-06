# random()

**Framework**: Swift  
**Kind**: method

Returns a random Boolean value.

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
static func random() -> Bool
```

#### Return Value

Either `true` or `false`, randomly chosen with equal probability.

#### Discussion

This method returns `true` and `false` with equal probability.

```swift
let flippedHeads = Bool.random()
if flippedHeads {
    print("Heads, you win!")
} else {
    print("Maybe another try?")
}
```

This method is equivalent to calling `Bool.random(using:)`, passing in the system’s default random generator.

## See Also

- [static func random<T>(using: inout T) -> Bool](bool/random(using:).md)
  Returns a random Boolean value, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bool/random())*