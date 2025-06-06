# IteratorProtocol

**Framework**: Swift  
**Kind**: protocol

A type that supplies the values of a sequence one at a time.

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
protocol IteratorProtocol<Element>
```

#### Overview

The `IteratorProtocol` protocol is tightly linked with the `Sequence` protocol. Sequences provide access to their elements by creating an iterator, which keeps track of its iteration process and returns one element at a time as it advances through the sequence.

Whenever you use a `for`-`in` loop with an array, set, or any other collection or sequence, you’re using that type’s iterator. Swift uses a sequence’s or collection’s iterator internally to enable the `for`-`in` loop language construct.

Using a sequence’s iterator directly gives you access to the same elements in the same order as iterating over that sequence using a `for`-`in` loop. For example, you might typically use a `for`-`in` loop to print each of the elements in an array.

```swift
let animals = ["Antelope", "Butterfly", "Camel", "Dolphin"]
for animal in animals {
    print(animal)
}
// Prints "Antelope"
// Prints "Butterfly"
// Prints "Camel"
// Prints "Dolphin"
```

Behind the scenes, Swift uses the `animals` array’s iterator to loop over the contents of the array.

```swift
var animalIterator = animals.makeIterator()
while let animal = animalIterator.next() {
    print(animal)
}
// Prints "Antelope"
// Prints "Butterfly"
// Prints "Camel"
// Prints "Dolphin"
```

The call to `animals.makeIterator()` returns an instance of the array’s iterator. Next, the `while` loop calls the iterator’s `next()` method repeatedly, binding each element that is returned to `animal` and exiting when the `next()` method returns `nil`.

### Using Iterators Directly

You rarely need to use iterators directly, because a `for`-`in` loop is the more idiomatic approach to traversing a sequence in Swift. Some algorithms, however, may call for direct iterator use.

One example is the `reduce1(_:)` method. Similar to the `reduce(_:_:)` method defined in the standard library, which takes an initial value and a combining closure, `reduce1(_:)` uses the first element of the sequence as the initial value.

Here’s an implementation of the `reduce1(_:)` method. The sequence’s iterator is used directly to retrieve the initial value before looping over the rest of the sequence.

```swift
extension Sequence {
    func reduce1(
        _ nextPartialResult: (Element, Element) -> Element
    ) -> Element?
    {
        var i = makeIterator()
        guard var accumulated = i.next() else {
            return nil
        }

        while let element = i.next() {
            accumulated = nextPartialResult(accumulated, element)
        }
        return accumulated
    }
}
```

The `reduce1(_:)` method makes certain kinds of sequence operations simpler. Here’s how to find the longest string in a sequence, using the `animals` array introduced earlier as an example:

```swift
let longestAnimal = animals.reduce1 { current, element in
    if current.count > element.count {
        return current
    } else {
        return element
    }
}
print(longestAnimal)
// Prints Optional("Butterfly")
```

### Using Multiple Iterators

Whenever you use multiple iterators (or `for`-`in` loops) over a single sequence, be sure you know that the specific sequence supports repeated iteration, either because you know its concrete type or because the sequence is also constrained to the `Collection` protocol.

Obtain each separate iterator from separate calls to the sequence’s `makeIterator()` method rather than by copying. Copying an iterator is safe, but advancing one copy of an iterator by calling its `next()` method may invalidate other copies of that iterator. `for`-`in` loops are safe in this regard.

### Adding Iteratorprotocol Conformance to Your Type

Implementing an iterator that conforms to `IteratorProtocol` is simple. Declare a `next()` method that advances one step in the related sequence and returns the current element. When the sequence has been exhausted, the `next()` method returns `nil`.

For example, consider a custom `Countdown` sequence. You can initialize the `Countdown` sequence with a starting integer and then iterate over the count down to zero. The `Countdown` structure’s definition is short: It contains only the starting count and the `makeIterator()` method required by the `Sequence` protocol.

```swift
struct Countdown: Sequence {
    let start: Int

    func makeIterator() -> CountdownIterator {
        return CountdownIterator(self)
    }
}
```

The `makeIterator()` method returns another custom type, an iterator named `CountdownIterator`. The `CountdownIterator` type keeps track of both the `Countdown` sequence that it’s iterating and the number of times it has returned a value.

```swift
struct CountdownIterator: IteratorProtocol {
    let countdown: Countdown
    var times = 0

    init(_ countdown: Countdown) {
        self.countdown = countdown
    }

    mutating func next() -> Int? {
        let nextNumber = countdown.start - times
        guard nextNumber > 0
            else { return nil }

        times += 1
        return nextNumber
    }
}
```

Each time the `next()` method is called on a `CountdownIterator` instance, it calculates the new next value, checks to see whether it has reached zero, and then returns either the number, or `nil` if the iterator is finished returning elements of the sequence.

Creating and iterating over a `Countdown` sequence uses a `CountdownIterator` to handle the iteration.

```swift
let threeTwoOne = Countdown(start: 3)
for count in threeTwoOne {
    print("\(count)...")
}
// Prints "3..."
// Prints "2..."
// Prints "1..."
```

## Topics

### Associated Types
- [associatedtype Element](iteratorprotocol/element.md)
  The type of element traversed by the iterator.
### Instance Methods
- [func next() -> Self.Element?](iteratorprotocol/next.md)
  Advances to the next element and returns it, or `nil` if no next element exists.

## Relationships

### Conforming Types
- [AnyIterator](anyiterator.md)
- [CollectionOfOne.Iterator](collectionofone/iterator.md)
- [Dictionary.Iterator](dictionary/iterator.md)
- [Dictionary.Keys.Iterator](dictionary/keys-swift.struct/iterator.md)
- [Dictionary.Values.Iterator](dictionary/values-swift.struct/iterator.md)
- [DropWhileSequence.Iterator](dropwhilesequence/iterator.md)
- [EmptyCollection.Iterator](emptycollection/iterator.md)
- [EnumeratedSequence.Iterator](enumeratedsequence/iterator.md)
- [FlattenSequence.Iterator](flattensequence/iterator.md)
- [IndexingIterator](indexingiterator.md)
- [IteratorSequence](iteratorsequence.md)
- [JoinedSequence.Iterator](joinedsequence/iterator.md)
- [LazyDropWhileSequence.Iterator](lazydropwhilesequence/iterator.md)
- [LazyFilterSequence.Iterator](lazyfiltersequence/iterator.md)
- [LazyMapSequence.Iterator](lazymapsequence/iterator.md)
- [LazyPrefixWhileSequence.Iterator](lazyprefixwhilesequence/iterator.md)
- [PartialRangeFrom.Iterator](partialrangefrom/iterator.md)
- [PrefixSequence.Iterator](prefixsequence/iterator.md)
- [ReversedCollection.Iterator](reversedcollection/iterator.md)
- [Set.Iterator](set/iterator.md)
- [StrideThroughIterator](stridethroughiterator.md)
- [StrideToIterator](stridetoiterator.md)
- [String.Iterator](string/iterator.md)
- [String.UTF16View.Iterator](string/utf16view/iterator.md)
- [String.UnicodeScalarView.Iterator](string/unicodescalarview/iterator.md)
- [UnfoldSequence](unfoldsequence.md)
- [UnsafeBufferPointer.Iterator](unsafebufferpointer/iterator.md)
- [UnsafeRawBufferPointer.Iterator](unsaferawbufferpointer/iterator.md)
- [Zip2Sequence.Iterator](zip2sequence/iterator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/iteratorprotocol)*