# dropFirst(_:)

**Framework**: Group Activities  
**Kind**: method

Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func dropFirst(_ count: Int = 1) -> AsyncDropFirstSequence<Self>
```

#### Return Value

An asynchronous sequence that drops the first `count` elements from the base sequence.

#### Discussion

Use `dropFirst(_:)` when you want to drop the first  elements from the base sequence and pass through the remaining elements.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `dropFirst(_:)` method causes the modified sequence to ignore the values `1` through `3`, and instead emit `4` through `10`:

```swift
for await number in Counter(howHigh: 10).dropFirst(3) {
    print(number, terminator: " ")
}
// Prints "4 5 6 7 8 9 10 "
```

If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

## Parameters

- `count`: The number of elements to drop from the beginning of   the sequence.   must be greater than or equal to zero.

## See Also

- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](groupsessionmessenger/messages/drop(while:).md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](groupsessionmessenger/messages/filter(_:).md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/messages/dropfirst(_:))*