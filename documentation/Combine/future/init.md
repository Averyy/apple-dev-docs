# init(_:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that invokes a promise closure when the publisher emits an element.

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
init(_ attemptToFulfill: @escaping (@escaping Future<Output, Failure>.Promise) -> Void)
```

## Parameters

- `attemptToFulfill`: A   that the publisher invokes when the publisher emits an element or terminates with an error.

## See Also

- [typealias Promise](future/promise.md)
  A type that represents a closure to invoke in the future, when an element or error is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/future/init(_:))*