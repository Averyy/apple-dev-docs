# Empty

**Framework**: Combine  
**Kind**: struct

A publisher that never publishes any values, and optionally finishes immediately.

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
struct Empty<Output, Failure> where Failure : Error
```

#### Overview

You can create a ”Never” publisher — one which never sends values and never finishes or fails — with the initializer `Empty(completeImmediately: false)`.

## Topics

### Creating an Empty Publisher
- [init(completeImmediately: Bool)](empty/init(completeimmediately:).md)
  Creates an empty publisher.
- [init(completeImmediately: Bool, outputType: Output.Type, failureType: Failure.Type)](empty/init(completeimmediately:outputtype:failuretype:).md)
  Creates an empty publisher with the given completion behavior and output and failure types.
### Inspecting Publisher Properties
- [let completeImmediately: Bool](empty/completeimmediately.md)
  A Boolean value that indicates whether the publisher immediately sends a completion.
### Comparing Publishers
- [static func == (Empty<Output, Failure>, Empty<Output, Failure>) -> Bool](empty/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](empty/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](empty-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](empty/equatable-implementations.md)
- [Publisher Implementations](empty/publisher-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [class Future](future.md)
  A publisher that eventually produces a single value and then finishes or fails.
- [struct Just](just.md)
  A publisher that emits an output to each subscriber just once, and then finishes.
- [struct Deferred](deferred.md)
  A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [struct Fail](fail.md)
  A publisher that immediately terminates with the specified error.
- [struct Record](record.md)
  A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/empty)*