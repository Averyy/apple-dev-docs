# shuffled()

**Framework**: RealityKit  
**Kind**: method

Returns the elements of the sequence, shuffled.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func shuffled() -> [Self.Element]
```

#### Return Value

A shuffled array of this sequence’s elements.

#### Discussion

For example, you can shuffle the numbers between `0` and `9` by calling the `shuffled()` method on that range:

```None
let numbers = 0...9
let shuffledNumbers = numbers.shuffled()
// shuffledNumbers == [1, 7, 6, 2, 8, 9, 4, 3, 5, 0]
```

This method is equivalent to calling `shuffled(using:)`, passing in the system’s default random generator.

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## See Also

- [func shuffled<T>(using: inout T) -> [Self.Element]](queryresult/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult/shuffled())*