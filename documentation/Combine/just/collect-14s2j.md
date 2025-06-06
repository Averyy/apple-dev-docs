# collect()

**Framework**: Combine  
**Kind**: method

Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.

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
func collect() -> Publishers.Collect<Self>
```

#### Return Value

A publisher that collects all received items and returns them as an array upon completion.

#### Discussion

Use [`collect()`](publisher/collect().md) to gather elements into an array that the operator emits after the upstream publisher finishes.

If the upstream publisher fails with an error, this publisher forwards the error to the downstream receiver instead of sending its output.

This publisher requests an unlimited number of elements from the upstream publisher and uses an unbounded amount of memory to store the received values. The publisher may exert memory pressure on the system for very large sets of elements.

The [`collect()`](publisher/collect().md) operator only sends the collected array to its downstream receiver after a request whose demand is greater than 0 items. Otherwise, [`collect()`](publisher/collect().md) waits until it receives a non-zero request.

In the example below, an Integer range is a publisher that emits an array of integers:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .collect()
    .sink { print("\($0)") }

// Prints: "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/collect()-14s2j)*