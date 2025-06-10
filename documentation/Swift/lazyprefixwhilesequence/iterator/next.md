# next()

**Framework**: Swift  
**Kind**: method

Advances to the next element and returns it, or `nil` if no next element exists.

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
mutating func next() -> LazyPrefixWhileSequence<Base>.Iterator.Element?
```

#### Return Value

The next element in the underlying sequence, if a next element exists; otherwise, `nil`.

#### Discussion

Repeatedly calling this method returns, in order, all the elements of the underlying sequence. As soon as the sequence has run out of elements, all subsequent calls return `nil`.

You must not call this method if any other copy of this iterator has been advanced with a call to its `next()` method.

The following example shows how an iterator can be used explicitly to emulate a `for`-`in` loop. First, retrieve a sequence’s iterator, and then call the iterator’s `next()` method until it returns `nil`.

```swift
let numbers = [2, 3, 5, 7]
var numbersIterator = numbers.makeIterator()

while let num = numbersIterator.next() {
    print(num)
}
// Prints "2"
// Prints "3"
// Prints "5"
// Prints "7"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/iterator/next())*