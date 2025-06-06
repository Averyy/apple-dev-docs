# prepend(_:)

**Framework**: Combine  
**Kind**: method

Prefixes a publisher’s output with the specified values.

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
func prepend(_ elements: Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>
```

#### Return Value

A publisher that prefixes the specified elements prior to this publisher’s elements.

#### Discussion

Use [`prepend(_:)`](publisher/prepend(_:)-7wk5l.md) when you need to prepend specific elements before the output of a publisher.

In the example below, the [`prepend(_:)`](publisher/prepend(_:)-7wk5l.md) operator publishes the provided elements before republishing all elements from `dataElements`:

```swift
let dataElements = (0...10)
cancellable = dataElements.publisher
    .prepend(0, 1, 255)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 255 0 1 2 3 4 5 6 7 8 9 10"
```

## Parameters

- `elements`: The elements to publish before this publisher’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/deferred/prepend(_:)-8y5ex)*