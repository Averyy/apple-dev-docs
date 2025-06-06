# Just

**Framework**: Combine  
**Kind**: struct

A publisher that emits an output to each subscriber just once, and then finishes.

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
struct Just<Output>
```

#### Overview

You can use a [`Just`](just.md) publisher to start a chain of publishers. A [`Just`](just.md) publisher is also useful when replacing a value with [`Publishers.Catch`](publishers/catch.md).

In contrast with [`Result.Publisher`](https://developer.apple.com/documentation/Swift/Result/Publisher-swift.struct), a [`Just`](just.md) publisher can’t fail with an error. And unlike [`Optional.Publisher`](https://developer.apple.com/documentation/Swift/Optional/Publisher-swift.struct), a [`Just`](just.md) publisher always produces a value.

## Topics

### Creating a Just Publisher
- [init(Output)](just/init(_:).md)
  Initializes a publisher that emits the specified output just once.
### Declaring Publisher Topography
- [typealias Failure](just/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let output: Output](just/output.md)
  The one element that the publisher emits.
### Comparing Publishers
- [static func == (Just<Output>, Just<Output>) -> Bool](just/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](just/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](just-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](just/equatable-implementations.md)
- [Publisher Implementations](just/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [class Future](future.md)
  A publisher that eventually produces a single value and then finishes or fails.
- [struct Deferred](deferred.md)
  A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [struct Empty](empty.md)
  A publisher that never publishes any values, and optionally finishes immediately.
- [struct Fail](fail.md)
  A publisher that immediately terminates with the specified error.
- [struct Record](record.md)
  A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just)*