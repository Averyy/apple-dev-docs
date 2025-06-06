# partition(by:)

**Framework**: Swift  
**Kind**: method

Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.

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
mutating func partition(by belongsInSecondPartition: (Self.Element) throws -> Bool) rethrows -> Self.Index
```

#### Return Value

The index of the first element in the reordered collection that matches `belongsInSecondPartition`. If no elements in the collection match `belongsInSecondPartition`, the returned index is equal to the collection’s `endIndex`.

#### Discussion

After partitioning a collection, there is a pivot index `p` where no element before `p` satisfies the `belongsInSecondPartition` predicate and every element at or after `p` satisfies `belongsInSecondPartition`. This operation isn’t guaranteed to be stable, so the relative ordering of elements within the partitions might change.

In the following example, an array of numbers is partitioned by a predicate that matches elements greater than 30.

```swift
var numbers = [30, 40, 20, 30, 30, 60, 10]
let p = numbers.partition(by: { $0 > 30 })
// p == 5
// numbers == [30, 10, 20, 30, 30, 60, 40]
```

The `numbers` array is now arranged in two partitions. The first partition, `numbers[..<p]`, is made up of the elements that are not greater than 30. The second partition, `numbers[p...]`, is made up of the elements that  greater than 30.

```swift
let first = numbers[..<p]
// first == [30, 10, 20, 30, 30]
let second = numbers[p...]
// second == [60, 40]
```

Note that the order of elements in both partitions changed. That is, `40` appears before `60` in the original collection, but, after calling `partition(by:)`, `60` appears before `40`.

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `belongsInSecondPartition`: A predicate used to partition   the collection. All elements satisfying this predicate are ordered   after all elements not satisfying it.

## See Also

- [func sort()](array/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](array/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sorted() -> [Self.Element]](array/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](array/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reverse()](array/reverse.md)
  Reverses the elements of the collection in place.
- [func reversed() -> ReversedCollection<Self>](array/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func shuffle()](array/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](array/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func shuffled() -> [Self.Element]](array/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](array/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func swapAt(Self.Index, Self.Index)](array/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/partition(by:)-90po8)*