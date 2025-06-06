# prepend(_:)

**Framework**: Combine  
**Kind**: method

Prefixes a publisher’s output with the specified sequence.

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
func prepend<S>(_ elements: S) -> Publishers.Concatenate<Publishers.Sequence<S, Self.Failure>, Self> where S : Sequence, Self.Output == S.Element
```

#### Return Value

A publisher that prefixes the sequence of elements prior to this publisher’s elements.

#### Discussion

Use [`prepend(_:)`](publisher/prepend(_:)-v9sb.md) to publish values from two publishers when you need to prepend one publisher’s elements to another.

In this example the [`prepend(_:)`](publisher/prepend(_:)-v9sb.md) operator publishes the provided sequence before republishing all elements from `dataElements`:

```swift
let prefixValues = [0, 1, 255]
let dataElements = (0...10)
cancellable = dataElements.publisher
    .prepend(prefixValues)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 255 0 1 2 3 4 5 6 7 8 9 10"
```

## Parameters

- `elements`: A sequence of elements to publish before this publisher’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/future/prepend(_:)-4n5i5)*