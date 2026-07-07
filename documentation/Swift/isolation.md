# isolation()

**Framework**: Swift  
**Kind**: macro

Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.

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
@freestanding
(expression) macro isolation<T>() -> T
```

#### Overview

If the type annotation provided for `#isolation` is not `(any Actor)?`, the type must match the enclosing actor type. If no type annotation is provided, the type defaults to `(any Actor)?`.

## See Also

- [protocol Sendable](sendable.md)
  A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [protocol Actor](actor.md)
  Common protocol to which all actors conform.
- [actor MainActor](mainactor.md)
  A singleton actor whose executor is equivalent to the main dispatch queue.
- [protocol GlobalActor](globalactor.md)
  A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [protocol SendableMetatype](sendablemetatype.md)
  A type whose metatype can be shared across arbitrary isolation domains without introducing a risk of data races.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/isolation())*