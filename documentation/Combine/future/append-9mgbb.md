# append(_:)

**Framework**: Combine  
**Kind**: method

Appends a publisher’s output with the specified elements.

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
func append(_ elements: Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>
```

#### Return Value

A publisher that appends the specifiecd elements after this publisher’s elements.

#### Discussion

Use [`append(_:)`](publisher/append(_:)-1qb8d.md) when you need to prepend specific elements after the output of a publisher.

In the example below, the [`append(_:)`](publisher/append(_:)-1qb8d.md) operator publishes the provided elements after republishing all elements from `dataElements`:

```swift
let dataElements = (0...10)
cancellable = dataElements.publisher
    .append(0, 1, 255)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 2 3 4 5 6 7 8 9 10 0 1 255"
```

## Parameters

- `elements`: Elements to publish after this publisher’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/future/append(_:)-9mgbb)*