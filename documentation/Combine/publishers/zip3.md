# Publishers.Zip3

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher created by applying the zip function to three upstream publishers.

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
struct Zip3<A, B, C> where A : Publisher, B : Publisher, C : Publisher, A.Failure == B.Failure, B.Failure == C.Failure
```

## Overview

Use a `Publishers.Zip3` to combine the latest elements from three publishers and emit a tuple to the downstream. The returned publisher waits until all three publishers have emitted an event, then delivers the oldest unconsumed event from each publisher as a tuple to the subscriber.

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## Topics

### Creating a zip-three Publisher
- [init(A, B, C)](./zip3/init%28_,_,_%29.md)
  Creates a publisher that applies the zip function to three upstream publishers.
### Declaring supporting types
- [Publishers.Zip3.Output](./zip3/output.md)
  The kind of values published by this publisher.
- [Publishers.Zip3.Failure](./zip3/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](./zip3/a.md)
  A publisher to zip.
- [let b: B](./zip3/b.md)
  A second publisher to zip.
- [let c: C](./zip3/c.md)
  A third publisher to zip.
### Comparing publishers
- [static func == (Publishers.Zip3<A, B, C>, Publishers.Zip3<A, B, C>) -> Bool](./zip3/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./zip3/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Combining elements from multiple publishers
- [Publishers.CombineLatest](./combinelatest.md)
  A publisher that receives and combines the latest elements from two publishers.
- [Publishers.CombineLatest3](./combinelatest3.md)
  A publisher that receives and combines the latest elements from three publishers.
- [Publishers.CombineLatest4](./combinelatest4.md)
  A publisher that receives and combines the latest elements from four publishers.
- [Publishers.Merge](./merge.md)
  A publisher created by applying the merge function to two upstream publishers.
- [Publishers.Merge3](./merge3.md)
  A publisher created by applying the merge function to three upstream publishers.
- [Publishers.Merge4](./merge4.md)
  A publisher created by applying the merge function to four upstream publishers.
- [Publishers.Merge5](./merge5.md)
  A publisher created by applying the merge function to five upstream publishers.
- [Publishers.Merge6](./merge6.md)
  A publisher created by applying the merge function to six upstream publishers.
- [Publishers.Merge7](./merge7.md)
  A publisher created by applying the merge function to seven upstream publishers.
- [Publishers.Merge8](./merge8.md)
  A publisher created by applying the merge function to eight upstream publishers.
- [Publishers.MergeMany](./mergemany.md)
  A publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [Publishers.Zip](./zip.md)
  A publisher created by applying the zip function to two upstream publishers.
- [Publishers.Zip4](./zip4.md)
  A publisher created by applying the zip function to four upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip3)*