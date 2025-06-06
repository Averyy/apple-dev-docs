# first()

**Framework**: Combine  
**Kind**: method

Publishes the first element of a stream, then finishes.

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
func first() -> Publishers.First<Self>
```

#### Return Value

A publisher that only publishes the first element of a stream.

#### Discussion

Use [`first()`](publisher/first().md) to publish just the first element from an upstream publisher, then finish normally. The [`first()`](publisher/first().md) operator requests [`unlimited`](subscribers/demand/unlimited.md) from its upstream as soon as downstream requests at least one element. If the upstream completes before [`first()`](publisher/first().md) receives any elements, it completes without emitting any values.

In this example, the [`first()`](publisher/first().md) publisher republishes the first element received from the sequence publisher, `-10`, then finishes normally.

```swift
let numbers = (-10...10)
cancellable = numbers.publisher
    .first()
    .sink { print("\($0)") }

// Print: "-10"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/first()-5fjpo)*