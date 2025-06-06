# append(_:)

**Framework**: Combine  
**Kind**: method

Appends a publisher’s output with the specified sequence.

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
func append<S>(_ elements: S) -> Publishers.Concatenate<Self, Publishers.Sequence<S, Self.Failure>> where S : Sequence, Self.Output == S.Element
```

#### Return Value

A publisher that appends the sequence of elements after this publisher’s elements.

#### Discussion

Use [`append(_:)`](publisher/append(_:)-69sdn.md) to append a sequence to the end of a publisher’s output.

In the example below, the [`append(_:)`](publisher/append(_:)-69sdn.md) publisher republishes all elements from `groundTransport` until it finishes, then publishes the members of `airTransport`:

```swift
let groundTransport = ["car", "bus", "truck", "subway", "bicycle"]
let airTransport = ["parasail", "jet", "helicopter", "rocket"]
cancellable = groundTransport.publisher
    .append(airTransport)
    .sink { print("\($0)", terminator: " ") }

// Prints: "car bus truck subway bicycle parasail jet helicopter rocket"
```

## Parameters

- `elements`: A sequence of elements to publish after this publisher’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/passthroughsubject/append(_:)-dtrl)*