# Publishers.Contains

**Framework**: Combine  
**Kind**: struct

A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.

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
struct Contains<Upstream> where Upstream : Publisher, Upstream.Output : Equatable
```

## Topics

### Creating a Contains Publisher
- [init(upstream: Upstream, output: Upstream.Output)](publishers/contains/init(upstream:output:).md)
  Creates a publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
### Declaring Publisher Topography
- [Publishers.Contains.Output](publishers/contains/output-swift.typealias.md)
  The kind of values published by this publisher.
- [Publishers.Contains.Failure](publishers/contains/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/contains/upstream.md)
  The publisher from which this publisher receives elements.
- [let output: Upstream.Output](publishers/contains/output-swift.property.md)
  The element to match in the upstream publisher.
### Comparing Publishers
- [static func == (Publishers.Contains<Upstream>, Publishers.Contains<Upstream>) -> Bool](publishers/contains/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](publishers/contains/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](publishers-contains-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](publishers/contains/equatable-implementations.md)
- [Publisher Implementations](publishers/contains/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.ContainsWhere](publishers/containswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [Publishers.TryContainsWhere](publishers/trycontainswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [Publishers.AllSatisfy](publishers/allsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [Publishers.TryAllSatisfy](publishers/tryallsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/contains)*