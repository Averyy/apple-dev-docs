# sequence(first:next:)

**Framework**: Swift  
**Kind**: func

Returns a sequence formed from `first` and repeated lazy applications of `next`.

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
func sequence<T>(first: T, next: @escaping (T) -> T?) -> UnfoldFirstSequence<T>
```

#### Return Value

A sequence that starts with `first` and continues with every value returned by passing the previous element to `next`.

#### Discussion

The first element in the sequence is always `first`, and each successive element is the result of invoking `next` with the previous element. The sequence ends when `next` returns `nil`. If `next` never returns `nil`, the sequence is infinite.

This function can be used to replace many cases that were previously handled using C-style `for` loops.

Example:

```swift
// Walk the elements of a tree from a node up to the root
for node in sequence(first: leaf, next: { $0.parent }) {
  // node is leaf, then leaf.parent, then leaf.parent.parent, etc.
}

// Iterate over all powers of two (ignoring overflow)
for value in sequence(first: 1, next: { $0 * 2 }) {
  // value is 1, then 2, then 4, then 8, etc.
}
```

## Parameters

- `first`: The first element to be returned from the sequence.
- `next`: A closure that accepts the previous sequence element and   returns the next element.

## See Also

- [func sequence<T, State>(state: State, next: (inout State) -> T?) -> UnfoldSequence<T, State>](sequence(state:next:).md)
  Returns a sequence formed from repeated lazy applications of `next` to a mutable `state`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence(first:next:))*