# Fail

**Framework**: Combine  
**Kind**: struct

A publisher that immediately terminates with the specified error.

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
struct Fail<Output, Failure> where Failure : Error
```

## Topics

### Creating a Fail Publisher
- [init(error: Failure)](fail/init(error:).md)
  Creates a publisher that immediately terminates with the specified failure.
- [init(outputType: Output.Type, failure: Failure)](fail/init(outputtype:failure:).md)
  Creates publisher with the given output type, that immediately terminates with the specified failure.
### Inspecting Publisher Properties
- [let error: Failure](fail/error.md)
  The failure to send when terminating the publisher.
### Comparing Publishers
- [static func == (Fail<Output, Failure>, Fail<Output, Failure>) -> Bool](fail/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](fail/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](fail-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](fail/equatable-implementations.md)
- [Publisher Implementations](fail/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [class Future](future.md)
  A publisher that eventually produces a single value and then finishes or fails.
- [struct Just](just.md)
  A publisher that emits an output to each subscriber just once, and then finishes.
- [struct Deferred](deferred.md)
  A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [struct Empty](empty.md)
  A publisher that never publishes any values, and optionally finishes immediately.
- [struct Record](record.md)
  A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/fail)*