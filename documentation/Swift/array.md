# Array

**Framework**: Swift  
**Kind**: struct

An ordered, random-access collection.

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
@frozen
struct Array<Element>
```

#### Overview

Arrays are one of the most commonly used data types in an app. You use arrays to organize your app’s data. Specifically, you use the `Array` type to hold elements of a single type, the array’s `Element` type. An array can store any kind of elements—from integers to strings to classes.

Swift makes it easy to create arrays in your code using an array literal: simply surround a comma-separated list of values with square brackets. Without any other information, Swift creates an array that includes the specified values, automatically inferring the array’s `Element` type. For example:

```swift
// An array of 'Int' elements
let oddNumbers = [1, 3, 5, 7, 9, 11, 13, 15]

// An array of 'String' elements
let streets = ["Albemarle", "Brandywine", "Chesapeake"]
```

You can create an empty array by specifying the `Element` type of your array in the declaration. For example:

```swift
// Shortened forms are preferred
var emptyDoubles: [Double] = []

// The full type name is also allowed
var emptyFloats: Array<Float> = Array()
```

If you need an array that is preinitialized with a fixed number of default values, use the `Array(repeating:count:)` initializer.

```swift
var digitCounts = Array(repeating: 0, count: 10)
print(digitCounts)
// Prints "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"
```

### Accessing Array Values

When you need to perform an operation on all of an array’s elements, use a `for`-`in` loop to iterate through the array’s contents.

```swift
for street in streets {
    print("I don't live on \(street).")
}
// Prints "I don't live on Albemarle."
// Prints "I don't live on Brandywine."
// Prints "I don't live on Chesapeake."
```

Use the `isEmpty` property to check quickly whether an array has any elements, or use the `count` property to find the number of elements in the array.

```swift
if oddNumbers.isEmpty {
    print("I don't know any odd numbers.")
} else {
    print("I know \(oddNumbers.count) odd numbers.")
}
// Prints "I know 8 odd numbers."
```

Use the `first` and `last` properties for safe access to the value of the array’s first and last elements. If the array is empty, these properties are `nil`.

```swift
if let firstElement = oddNumbers.first, let lastElement = oddNumbers.last {
    print(firstElement, lastElement, separator: ", ")
}
// Prints "1, 15"

print(emptyDoubles.first, emptyDoubles.last, separator: ", ")
// Prints "nil, nil"
```

You can access individual array elements through a subscript. The first element of a nonempty array is always at index zero. You can subscript an array with any integer from zero up to, but not including, the count of the array. Using a negative number or an index equal to or greater than `count` triggers a runtime error. For example:

```swift
print(oddNumbers[0], oddNumbers[3], separator: ", ")
// Prints "1, 7"

print(emptyDoubles[0])
// Triggers runtime error: Index out of range
```

### Adding and Removing Elements

Suppose you need to store a list of the names of students that are signed up for a class you’re teaching. During the registration period, you need to add and remove names as students add and drop the class.

```swift
var students = ["Ben", "Ivy", "Jordell"]
```

To add single elements to the end of an array, use the `append(_:)` method. Add multiple elements at the same time by passing another array or a sequence of any kind to the `append(contentsOf:)` method.

```swift
students.append("Maxime")
students.append(contentsOf: ["Shakia", "William"])
// ["Ben", "Ivy", "Jordell", "Maxime", "Shakia", "William"]
```

You can add new elements in the middle of an array by using the `insert(_:at:)` method for single elements and by using `insert(contentsOf:at:)` to insert multiple elements from another collection or array literal. The elements at that index and later indices are shifted back to make room.

```swift
students.insert("Liam", at: 3)
// ["Ben", "Ivy", "Jordell", "Liam", "Maxime", "Shakia", "William"]
```

To remove elements from an array, use the `remove(at:)`, `removeSubrange(_:)`, and `removeLast()` methods.

```swift
// Ben's family is moving to another state
students.remove(at: 0)
// ["Ivy", "Jordell", "Liam", "Maxime", "Shakia", "William"]

// William is signing up for a different class
students.removeLast()
// ["Ivy", "Jordell", "Liam", "Maxime", "Shakia"]
```

You can replace an existing element with a new value by assigning the new value to the subscript.

```swift
if let i = students.firstIndex(of: "Maxime") {
    students[i] = "Max"
}
// ["Ivy", "Jordell", "Liam", "Max", "Shakia"]
```

#### Growing the Size of an Array

Every array reserves a specific amount of memory to hold its contents. When you add elements to an array and that array begins to exceed its reserved capacity, the array allocates a larger region of memory and copies its elements into the new storage. The new storage is a multiple of the old storage’s size. This exponential growth strategy means that appending an element happens in constant time, averaging the performance of many append operations. Append operations that trigger reallocation have a performance cost, but they occur less and less often as the array grows larger.

If you know approximately how many elements you will need to store, use the `reserveCapacity(_:)` method before appending to the array to avoid intermediate reallocations. Use the `capacity` and `count` properties to determine how many more elements the array can store without allocating larger storage.

For arrays of most `Element` types, this storage is a contiguous block of memory. For arrays with an `Element` type that is a class or `@objc` protocol type, this storage can be a contiguous block of memory or an instance of `NSArray`. Because any arbitrary subclass of `NSArray` can become an `Array`, there are no guarantees about representation or efficiency in this case.

### Modifying Copies of Arrays

Each array has an independent value that includes the values of all of its elements. For simple types such as integers and other structures, this means that when you change a value in one array, the value of that element does not change in any copies of the array. For example:

```swift
var numbers = [1, 2, 3, 4, 5]
var numbersCopy = numbers
numbers[0] = 100
print(numbers)
// Prints "[100, 2, 3, 4, 5]"
print(numbersCopy)
// Prints "[1, 2, 3, 4, 5]"
```

If the elements in an array are instances of a class, the semantics are the same, though they might appear different at first. In this case, the values stored in the array are references to objects that live outside the array. If you change a reference to an object in one array, only that array has a reference to the new object. However, if two arrays contain references to the same object, you can observe changes to that object’s properties from both arrays. For example:

```swift
// An integer type with reference semantics
class IntegerReference {
    var value = 10
}
var firstIntegers = [IntegerReference(), IntegerReference()]
var secondIntegers = firstIntegers

// Modifications to an instance are visible from either array
firstIntegers[0].value = 100
print(secondIntegers[0].value)
// Prints "100"

// Replacements, additions, and removals are still visible
// only in the modified array
firstIntegers[0] = IntegerReference()
print(firstIntegers[0].value)
// Prints "10"
print(secondIntegers[0].value)
// Prints "100"
```

Arrays, like all variable-size collections in the standard library, use copy-on-write optimization. Multiple copies of an array share the same storage until you modify one of the copies. When that happens, the array being modified replaces its storage with a uniquely owned copy of itself, which is then modified in place. Optimizations are sometimes applied that can reduce the amount of copying.

This means that if an array is sharing storage with other copies, the first mutating operation on that array incurs the cost of copying the array. An array that is the sole owner of its storage can perform mutating operations in place.

In the example below, a `numbers` array is created along with two copies that share the same storage. When the original `numbers` array is modified, it makes a unique copy of its storage before making the modification. Further modifications to `numbers` are made in place, while the two copies continue to share the original storage.

```swift
var numbers = [1, 2, 3, 4, 5]
var firstCopy = numbers
var secondCopy = numbers

// The storage for 'numbers' is copied here
numbers[0] = 100
numbers[1] = 200
numbers[2] = 300
// 'numbers' is [100, 200, 300, 4, 5]
// 'firstCopy' and 'secondCopy' are [1, 2, 3, 4, 5]
```

### Bridging Between Array and Nsarray

When you need to access APIs that require data in an `NSArray` instance instead of `Array`, use the type-cast operator (`as`) to bridge your instance. For bridging to be possible, the `Element` type of your array must be a class, an `@objc` protocol (a protocol imported from Objective-C or marked with the `@objc` attribute), or a type that bridges to a Foundation type.

The following example shows how you can bridge an `Array` instance to `NSArray` to use the `write(to:atomically:)` method. In this example, the `colors` array can be bridged to `NSArray` because the `colors` array’s `String` elements bridge to `NSString`. The compiler prevents bridging the `moreColors` array, on the other hand, because its `Element` type is `Optional<String>`, which does  bridge to a Foundation type.

```swift
let colors = ["periwinkle", "rose", "moss"]
let moreColors: [String?] = ["ochre", "pine"]

let url = URL(fileURLWithPath: "names.plist")
(colors as NSArray).write(to: url, atomically: true)
// true

(moreColors as NSArray).write(to: url, atomically: true)
// error: cannot convert value of type '[String?]' to type 'NSArray'
```

Bridging from `Array` to `NSArray` takes O(1) time and O(1) space if the array’s elements are already instances of a class or an `@objc` protocol; otherwise, it takes O() time and space.

When the destination array’s element type is a class or an `@objc` protocol, bridging from `NSArray` to `Array` first calls the `copy(with:)` (`- copyWithZone:` in Objective-C) method on the array to get an immutable copy and then performs additional Swift bookkeeping work that takes O(1) time. For instances of `NSArray` that are already immutable, `copy(with:)` usually returns the same array in O(1) time; otherwise, the copying performance is unspecified. If `copy(with:)` returns the same array, the instances of `NSArray` and `Array` share storage using the same copy-on-write optimization that is used when two instances of `Array` share storage.

When the destination array’s element type is a nonclass type that bridges to a Foundation type, bridging from `NSArray` to `Array` performs a bridging copy of the elements to contiguous storage in O() time. For example, bridging from `NSArray` to `Array<Int>` performs such a copy. No further bridging is required when accessing elements of the `Array` instance.

> **Note**: The `ContiguousArray` and `ArraySlice` types are not bridged; instances of those types always have a contiguous block of memory as their storage.

## Topics

### Creating an Array
- [init()](array/init.md)
  Creates a new, empty array.
- [init<S>(S)](array/init(_:)-1ip9h.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](array/init(_:)-236cl.md)
  Creates an array containing the elements of a sequence.
- [init(repeating: Element, count: Int)](array/init(repeating:count:).md)
  Creates a new array containing the specified number of a single, repeated value.
- [init(unsafeUninitializedCapacity: Int, initializingWith: (inout UnsafeMutableBufferPointer<Element>, inout Int) throws -> Void) rethrows](array/init(unsafeuninitializedcapacity:initializingwith:).md)
  Creates an array with the specified capacity, then calls the given closure with a buffer covering the array’s uninitialized memory.
### Inspecting an Array
- [var isEmpty: Bool](array/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var count: Int](array/count.md)
  The number of elements in the array.
- [var capacity: Int](array/capacity.md)
  The total number of elements that the array can contain without allocating new storage.
### Accessing Elements
- [subscript(Int) -> Element](array/subscript(_:)-25iat.md)
  Accesses the element at the specified position.
- [var first: Self.Element?](array/first.md)
  The first element of the collection.
- [var last: Self.Element?](array/last.md)
  The last element of the collection.
- [subscript(Range<Int>) -> ArraySlice<Element>](array/subscript(_:)-53fvb.md)
  Accesses a contiguous subrange of the array’s elements.
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-3kwny.md)
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-4h7rl.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](array/subscript(_:)-3pmfg.md)
- [func randomElement() -> Self.Element?](array/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](array/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
### Adding Elements
- [func append(Element)](array/append(_:).md)
  Adds a new element at the end of the array.
- [func insert(Element, at: Int)](array/insert(_:at:).md)
  Inserts a new element at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](array/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func replaceSubrange<C>(Range<Int>, with: C)](array/replacesubrange(_:with:).md)
  Replaces a range of elements with the elements in the specified collection.
- [func replaceSubrange<C, R>(R, with: C)](array/replacesubrange(_:with:)-7293p.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](array/reservecapacity(_:).md)
  Reserves enough space to store the specified number of elements.
### Combining Arrays
- [func append<S>(contentsOf: S)](array/append(contentsof:).md)
  Adds the elements of a sequence to the end of the array.
- [func append<S>(contentsOf: S)](array/append(contentsof:)-9foli.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [static func + <Other>(Other, Self) -> Self](array/+(_:_:)-6h58k.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](array/+(_:_:)-n33n.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + (Array<Element>, Array<Element>) -> Array<Element>](array/+(_:_:).md)
- [static func + <Other>(Self, Other) -> Self](array/+(_:_:)-9fm5l.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](array/+=(_:_:)-676ib.md)
  Appends the elements of a sequence to a range-replaceable collection.
- [static func += (inout Array<Element>, Array<Element>)](array/+=(_:_:).md)
### Removing Elements
- [func remove(at: Int) -> Element](array/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeFirst() -> Self.Element](array/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](array/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](array/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](array/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](array/removesubrange(_:)-8may1.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](array/removesubrange(_:)-9twou.md)
  Removes the elements in the specified subrange from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](array/removeall(where:)-5k61r.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(keepingCapacity: Bool)](array/removeall(keepingcapacity:).md)
  Removes all elements from the array.
- [func popLast() -> Self.Element?](array/poplast.md)
  Removes and returns the last element of the collection.
### Finding Elements
- [func contains(Self.Element) -> Bool](array/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](array/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](array/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](array/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(of: Self.Element) -> Self.Index?](array/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func index(of: Self.Element) -> Self.Index?](array/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](array/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](array/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](array/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](array/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func min() -> Self.Element?](array/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](array/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max() -> Self.Element?](array/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](array/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
### Selecting Elements
- [func prefix(Int) -> Self.SubSequence](array/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](array/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](array/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](array/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](array/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](array/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Excluding Elements
- [func dropFirst(Int) -> Self.SubSequence](array/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](array/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](array/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
### Transforming an Array
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](array/flatmap(_:)-i3mr.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](array/flatmap(_:)-6chu8.md)
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](array/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](array/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](array/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](array/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
### Iterating Over an Array’s Elements
- [func forEach((Self.Element) throws -> Void) rethrows](array/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](array/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func makeIterator() -> IndexingIterator<Self>](array/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [var underestimatedCount: Int](array/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Reordering an Array’s Elements
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
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](array/partition(by:)-90po8.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func swapAt(Self.Index, Self.Index)](array/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
### Splitting and Joining Elements
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](array/split(separator:maxsplits:omittingemptysubsequences:)-3dgmv.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](array/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func joined() -> FlattenSequence<Self>](array/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](array/joined(separator:)-7uber.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](array/joined(separator:)-5do1g.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined(separator: String) -> String](array/joined(separator:)-1ckod.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
### Creating and Applying Differences
- [func applying(CollectionDifference<Self.Element>) -> Self?](array/applying(_:).md)
  Applies the given difference to this collection.
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](array/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](array/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
### Comparing Arrays
- [static func == (Array<Element>, Array<Element>) -> Bool](array/==(_:_:).md)
  Returns a Boolean value indicating whether two arrays contain the same elements in the same order.
- [static func != (Self, Self) -> Bool](array/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](array/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](array/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](array/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](array/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](array/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](array/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
### Manipulating Indices
- [var startIndex: Int](array/startindex.md)
  The position of the first element in a nonempty array.
- [var endIndex: Int](array/endindex.md)
  The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func index(after: Int) -> Int](array/index(after:).md)
  Returns the position immediately after the given index.
- [func formIndex(after: inout Int)](array/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(before: Int) -> Int](array/index(before:).md)
  Returns the position immediately before the given index.
- [func formIndex(before: inout Int)](array/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Int, offsetBy: Int) -> Int](array/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](array/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func index(Int, offsetBy: Int, limitedBy: Int) -> Int?](array/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](array/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: Int, to: Int) -> Int](array/distance(from:to:).md)
  Returns the distance between two indices.
### Accessing Underlying Storage
- [func withUnsafeBufferPointer<R, E>((UnsafeBufferPointer<Element>) throws(E) -> R) throws(E) -> R](array/withunsafebufferpointer(_:).md)
  Calls a closure with a pointer to the array’s contiguous storage.
- [func withUnsafeMutableBufferPointer<R, E>((inout UnsafeMutableBufferPointer<Element>) throws(E) -> R) throws(E) -> R](array/withunsafemutablebufferpointer(_:).md)
  Calls the given closure with a pointer to the array’s mutable contiguous storage.
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) rethrows -> R](array/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the array’s contiguous storage.
- [func withUnsafeMutableBytes<R>((UnsafeMutableRawBufferPointer) throws -> R) rethrows -> R](array/withunsafemutablebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the array’s mutable contiguous storage.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Element>) throws -> R) rethrows -> R?](array/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](array/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Encoding and Decoding
- [func encode(to: any Encoder) throws](array/encode(to:).md)
  Encodes the elements of this array into the given encoder in an unkeyed container.
- [init(from: any Decoder) throws](array/init(from:)-6rmxq.md)
  Creates a new array by decoding from the given decoder.
### Describing an Array
- [var description: String](array/description.md)
  A textual representation of the array and its elements.
- [var debugDescription: String](array/debugdescription.md)
  A textual representation of the array and its elements, suitable for debugging.
- [var customMirror: Mirror](array/custommirror.md)
  A mirror that reflects the array.
- [func hash(into: inout Hasher)](array/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Converting Between Arrays and Create ML Types
- [init(MLDataColumn<Element>)](array/init(_:)-2ln1a.md)
  Constructs an Array with the elements of a DataColumn.
- [init(MLUntypedColumn)](array/init(_:)-86ka8.md)
  Constructs an Array with the elements of an MLUntypedColumn.
- [init?(from: MLDataValue)](array/init(from:)-51fkv.md)
  Creates an instance of the conforming type from a data value.
- [var dataValue: MLDataValue](array/datavalue.md)
  The value of the conforming type’s instance wrapped in a data value.
- [static var dataValueType: MLDataValue.ValueType](array/datavaluetype.md)
  The underlying type the conforming type uses when it wraps itself in a data value.
### Related Array Types
- [struct ContiguousArray](contiguousarray.md)
  A contiguously stored array.
- [struct ArraySlice](arrayslice.md)
  A slice of an `Array`, `ContiguousArray`, or `ArraySlice` instance.
### Reference Types
- [class NSArray](../Foundation/NSArray.md)
  A static ordered collection of objects.
- [class NSMutableArray](../Foundation/NSMutableArray.md)
  A dynamic ordered collection of objects.
### Supporting Types
- [typealias Index](array/index.md)
  The index type for arrays, `Int`.
- [typealias Indices](array/indices.md)
  The type that represents the indices that are valid for subscripting an array, in ascending order.
- [typealias Iterator](array/iterator.md)
  The type that allows iteration over an array’s elements.
- [typealias ArrayLiteralElement](array/arrayliteralelement.md)
  The type of the elements of an array literal.
- [typealias SubSequence](array/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Infrequently Used Functionality
- [init(arrayLiteral: Element...)](array/init(arrayliteral:).md)
  Creates an array from the given array literal.
- [var hashValue: Int](array/hashvalue.md)
  The hash value.
### Initializers
- [init(fromSplitComplex: DSPSplitComplex, scale: Float, count: Int)](array/init(fromsplitcomplex:scale:count:)-5eirc.md)
  Creates a new array of single-precision values from a `DSPSplitComplex` structure.
- [init(fromSplitComplex: DSPDoubleSplitComplex, scale: Double, count: Int)](array/init(fromsplitcomplex:scale:count:)-5kgr3.md)
  Creates a new array of single-precision values from a `DSPDoubleSplitComplex` structure.
### Type Aliases
- [typealias Specification](array/specification.md)
- [typealias UnderlyingSequence](array/underlyingsequence.md)
- [typealias UnwrappedType](array/unwrappedtype.md)
- [typealias ValueType](array/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<Array<Element>>](array/defaultresolverspecification.md)
### Type Methods
- [static func monoscopicForVideoOutput() -> [CMTag]](array/monoscopicforvideooutput.md)
  Creates a collection of CMTags with the required tags to describe monoscopic video, where there is no stereo view, e.g. kCMTagStereoNone.
- [static func stereoscopicForVideoOutput() -> [CMTag]](array/stereoscopicforvideooutput.md)
  Creates a collection of CMTags with the required tags to describe basic stereoscopic video, where both left and right stereo eyes are present, e.g. kCMTagStereoLeftAndRight.
### Default Implementations
- [BidirectionalCollection Implementations](array/bidirectionalcollection-implementations.md)
- [Collection Implementations](array/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](array/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](array/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](array/customstringconvertible-implementations.md)
- [Decodable Implementations](array/decodable-implementations.md)
- [Encodable Implementations](array/encodable-implementations.md)
- [Equatable Implementations](array/equatable-implementations.md)
- [ExpressibleByArrayLiteral Implementations](array/expressiblebyarrayliteral-implementations.md)
- [Hashable Implementations](array/hashable-implementations.md)
- [MLDataValueConvertible Implementations](array/mldatavalueconvertible-implementations.md)
- [MutableCollection Implementations](array/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](array/randomaccesscollection-implementations.md)
- [RangeReplaceableCollection Implementations](array/rangereplaceablecollection-implementations.md)
- [RelationshipCollection Implementations](array/relationshipcollection-implementations.md)
- [ResultsCollection Implementations](array/resultscollection-implementations.md)
- [Sequence Implementations](array/sequence-implementations.md)

## Relationships

### Conforms To
- [AccelerateBuffer](../Accelerate/AccelerateBuffer.md)
- [AccelerateMutableBuffer](../Accelerate/AccelerateMutableBuffer.md)
- [AppExtensionScene](../ExtensionKit/AppExtensionScene.md)
- [BidirectionalCollection](bidirectionalcollection.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](cvararg.md)
- [Collection](collection.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [DataProtocol](../Foundation/DataProtocol.md)
- [Decodable](decodable.md)
- [DecodableWithConfiguration](../Foundation/DecodableWithConfiguration.md)
- [Encodable](encodable.md)
- [EncodableWithConfiguration](../Foundation/EncodableWithConfiguration.md)
- [Equatable](equatable.md)
- [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md)
- [Hashable](hashable.md)
- [MLDataValueConvertible](../CreateML/MLDataValueConvertible.md)
- [MutableCollection](mutablecollection.md)
- [MutableDataProtocol](../Foundation/MutableDataProtocol.md)
- [PositionScaleRange](../Charts/PositionScaleRange.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [RangeReplaceableCollection](rangereplaceablecollection.md)
- [RelationshipCollection](../SwiftData/RelationshipCollection.md)
- [ResultsCollection](../AppIntents/ResultsCollection.md)
- [ScaleDomain](../Charts/ScaleDomain.md)
- [ScaleRange](../Charts/ScaleRange.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

- [struct Int](int.md)
  A signed integer value type.
- [struct Double](double.md)
  A double-precision, floating-point value type.
- [struct String](string.md)
  A Unicode string value that is a collection of characters.
- [struct Dictionary](dictionary.md)
  A collection whose elements are key-value pairs.
- [Swift Standard Library](swift-standard-library.md)
  Solve complex problems and write high-performance, readable code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Swift/array)*