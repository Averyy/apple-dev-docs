# Publishers.Sequence

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that publishes a given sequence of elements.

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
struct Sequence<Elements, Failure> where Elements : Sequence, Failure : Error
```

## Overview

When the publisher exhausts the elements in the sequence, the next request causes the publisher to finish.

## Topics

### Creating a sequence publisher
- [init(sequence: Elements)](./sequence/init%28sequence%29.md)
  Creates a publisher for a sequence of elements.
### Declaring supporting types
- [Publishers.Output](./output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
### Inspecting publisher properties
- [let sequence: Elements](./sequence/sequence.md)
  The sequence of elements to publish.
### Comparing publishers
- [static func == (Publishers.Sequence<Elements, Failure>, Publishers.Sequence<Elements, Failure>) -> Bool](./sequence/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Applying Operators
- [Publisher Operators](../publishers-sequence-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](./sequence/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Convenience publishers
- [Publishers.Catch](./catch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence)*