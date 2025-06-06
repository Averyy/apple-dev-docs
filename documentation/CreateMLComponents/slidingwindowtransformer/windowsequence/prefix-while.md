# prefix(while:)

**Framework**: Create ML Components  
**Kind**: method

Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.

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
@preconcurrency
func prefix(while predicate: @escaping (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>
```

#### Return Value

An asynchronous sequence of the initial, consecutive elements that satisfy `predicate`.

#### Discussion

Use `prefix(while:)` to produce values while elements from the base sequence meet a condition you specify. The modified sequence ends when the predicate closure returns `false`.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `prefix(while:)` method causes the modified sequence to pass along values so long as they aren’t divisible by `2` and `3`. Upon reaching `6`, the sequence ends:

```None
let stream = Counter(howHigh: 10)
    .prefix { $0 % 2 != 0 || $0 % 3 != 0 }
for try await number in stream {
    print(number, terminator: " ")
}
// Prints "1 2 3 4 5 "
```

## Parameters

- `predicate`: A closure that takes an element as a parameter and   returns a Boolean value indicating whether the element should be   included in the modified sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindowtransformer/windowsequence/prefix(while:))*