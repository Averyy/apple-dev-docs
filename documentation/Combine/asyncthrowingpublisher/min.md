# min()

**Framework**: Combine  
**Kind**: method

Returns the minimum element in an asynchronous sequence of comparable elements.

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
@warn_unqualified_access
func min() async rethrows -> Self.Element?
```

#### Return Value

The sequence’s minimum element. If the sequence has no elements, returns `nil`.

#### Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `min()` method returns the minimum value of the sequence.

```swift
let min = await Counter(howHigh: 10)
    .min()
print(min ?? "none")
// Prints "1"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/asyncthrowingpublisher/min())*