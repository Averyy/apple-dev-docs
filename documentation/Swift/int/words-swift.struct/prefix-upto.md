# prefix(upTo:)

**Framework**: Swift  
**Kind**: method

Returns a subsequence from the start of the collection up to, but not including, the specified position.

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
func prefix(upTo end: Self.Index) -> Self.SubSequence
```

#### Return Value

A subsequence up to, but not including, the `end` position.

#### Discussion

The resulting subsequence  the element at the position `end`. The following example searches for the index of the number `40` in an array of integers, and then prints the prefix of the array up to, but not including, that index:

```swift
let numbers = [10, 20, 30, 40, 50, 60]
if let i = numbers.firstIndex(of: 40) {
    print(numbers.prefix(upTo: i))
}
// Prints "[10, 20, 30]"
```

Passing the collection’s starting index as the `end` parameter results in an empty subsequence.

```swift
print(numbers.prefix(upTo: numbers.startIndex))
// Prints "[]"
```

Using the `prefix(upTo:)` method is equivalent to using a partial half-open range as the collection’s subscript. The subscript notation is preferred over `prefix(upTo:)`.

```swift
if let i = numbers.firstIndex(of: 40) {
    print(numbers[..<i])
}
// Prints "[10, 20, 30]"
```

> **Note**: O(1)

O(1)

## Parameters

- `end`: The “past the end” index of the resulting subsequence.    must be a valid index of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/words-swift.struct/prefix(upto:))*