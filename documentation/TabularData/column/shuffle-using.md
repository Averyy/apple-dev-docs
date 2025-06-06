# shuffle(using:)

**Framework**: TabularData  
**Kind**: method

Shuffles the collection in place, using the given generator as a source for randomness.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func shuffle<T>(using generator: inout T) where T : RandomNumberGenerator
```

#### Discussion

You use this method to randomize the elements of a collection when you are using a custom random number generator. For example, you can use the `shuffle(using:)` method to randomly reorder the elements of an array.

```None
var names = ["Alejandro", "Camila", "Diego", "Luciana", "Luis", "Sofía"]
names.shuffle(using: &myGenerator)
// names == ["Sofía", "Alejandro", "Camila", "Luis", "Diego", "Luciana"]
```

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

> **Note**: The algorithm used to shuffle a collection may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

The algorithm used to shuffle a collection may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

## Parameters

- `generator`: The random number generator to use when shuffling   the collection.

## See Also

- [func shuffle()](column/shuffle.md)
  Shuffles the collection in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/shuffle(using:))*