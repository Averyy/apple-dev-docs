# Future.Promise

**Framework**: Combine  
**Kind**: typealias

A type that represents a closure to invoke in the future, when an element or error is available.

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
typealias Promise = (Result<Output, Failure>) -> Void
```

## Mentions

- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)

#### Discussion

The promise closure receives one parameter: a `Result` that contains either a single element published by a [`Future`](future.md), or an error.

## See Also

- [init((Future<Output, Failure>.Promise) -> Void)](future/init(_:).md)
  Creates a publisher that invokes a promise closure when the publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/future/promise)*