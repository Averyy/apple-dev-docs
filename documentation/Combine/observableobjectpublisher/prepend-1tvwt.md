# prepend(_:)

**Framework**: Combine  
**Kind**: method

Prefixes the output of this publisher with the elements emitted by the given publisher.

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
func prepend<P>(_ publisher: P) -> Publishers.Concatenate<P, Self> where P : Publisher, Self.Failure == P.Failure, Self.Output == P.Output
```

#### Return Value

A publisher that prefixes the prefixing publisher’s elements prior to this publisher’s elements.

#### Discussion

Use [`prepend(_:)`](publisher/prepend(_:)-5dj9c.md) to publish values from two publishers when you need to prepend one publisher’s elements to another.

In the example below, a publisher of `prefixValues` publishes its elements before the `dataElements` publishes its elements:

```swift
let prefixValues = [0, 1, 255]
let dataElements = (0...10)
cancellable = dataElements.publisher
    .prepend(prefixValues.publisher)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 255 0 1 2 3 4 5 6 7 8 9 10"
```

## Parameters

- `publisher`: The prefixing publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/observableobjectpublisher/prepend(_:)-1tvwt)*