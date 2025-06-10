# drop(while:)

**Framework**: Swift  
**Kind**: method

Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.

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
func drop(while predicate: @escaping (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>
```

#### Return Value

An asynchronous sequence that skips over values from the base sequence until the provided closure returns `false`.

#### Discussion

Use `drop(while:)` to omit elements from an asynchronous sequence until the element received meets a condition you specify.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `drop(while:)` method causes the modified sequence to ignore received values until it encounters one that is divisible by `3`:

```swift
let stream = Counter(howHigh: 10)
    .drop { $0 % 3 != 0 }
for await number in stream {
    print(number, terminator: " ")
}
// Prints "3 4 5 6 7 8 9 10 "
```

After the predicate returns `false`, the sequence never executes it again, and from then on the sequence passes through elements from its underlying sequence as-is.

## Parameters

- `predicate`: A closure that takes an element as a parameter and   returns a Boolean value indicating whether to drop the element from the   modified sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingcompactmapsequence/drop(while:))*