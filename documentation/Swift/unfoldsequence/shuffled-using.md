# shuffled(using:)

**Framework**: Swift  
**Kind**: method

Returns the elements of the sequence, shuffled using the given generator as a source for randomness.

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
func shuffled<T>(using generator: inout T) -> [Self.Element] where T : RandomNumberGenerator
```

#### Return Value

An array of this sequence’s elements in a shuffled order.

#### Discussion

You use this method to randomize the elements of a sequence when you are using a custom random number generator. For example, you can shuffle the numbers between `0` and `9` by calling the `shuffled(using:)` method on that range:

```swift
let numbers = 0...9
let shuffledNumbers = numbers.shuffled(using: &myGenerator)
// shuffledNumbers == [8, 9, 4, 3, 2, 6, 7, 0, 5, 1]
```

> **Note**: O(), where  is the length of the sequence.

> **Note**: The algorithm used to shuffle a sequence may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

## Parameters

- `generator`: The random number generator to use when shuffling   the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unfoldsequence/shuffled(using:))*