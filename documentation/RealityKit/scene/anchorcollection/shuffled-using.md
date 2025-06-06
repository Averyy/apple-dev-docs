# shuffled(using:)

**Framework**: RealityKit  
**Kind**: method

Returns the elements of the sequence, shuffled using the given generator as a source for randomness.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func shuffled<T>(using generator: inout T) -> [Self.Element] where T : RandomNumberGenerator
```

#### Return Value

An array of this sequence’s elements in a shuffled order.

#### Discussion

You use this method to randomize the elements of a sequence when you are using a custom random number generator. For example, you can shuffle the numbers between `0` and `9` by calling the `shuffled(using:)` method on that range:

```None
let numbers = 0...9
let shuffledNumbers = numbers.shuffled(using: &myGenerator)
// shuffledNumbers == [8, 9, 4, 3, 2, 6, 7, 0, 5, 1]
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

> **Note**: The algorithm used to shuffle a sequence may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

The algorithm used to shuffle a sequence may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

## Parameters

- `generator`: The random number generator to use when shuffling   the sequence.

## See Also

- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](scene/anchorcollection/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reversed() -> [Self.Element]](scene/anchorcollection/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](scene/anchorcollection/shuffled.md)
  Returns the elements of the sequence, shuffled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/shuffled(using:))*