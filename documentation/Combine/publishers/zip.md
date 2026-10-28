# Publishers.Zip

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher created by applying the zip function to two upstream publishers.

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
struct Zip<A, B> where A : Publisher, B : Publisher, A.Failure == B.Failure
```

## Overview

Use `Publishers.Zip` to combine the latest elements from two publishers and emit a tuple to the downstream. The returned publisher waits until both publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together as a tuple to the subscriber.

Much like a zipper or zip fastener on a piece of clothing pulls together rows of teeth to link the two sides, `Publishers.Zip` combines streams from two different publishers by linking pairs of elements from each side.

If either upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## Topics

### Creating a zip publisher
- [init(_:_:)](./zip/init%28_,_%29.md)
  Creates a publisher that applies the zip function to two upstream publishers.
### Declaring supporting types
- [Publishers.Zip.Output](./zip/output.md)
  The kind of values published by this publisher.
- [Publishers.Zip.Failure](./zip/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](./zip/a.md)
  A publisher to zip.
- [let b: B](./zip/b.md)
  Another publisher to zip.
### Comparing publishers
- [static func == (Publishers.Zip<A, B>, Publishers.Zip<A, B>) -> Bool](./zip/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./zip/equatable-implementations.md)

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
- [Publishers.Zip3](./zip3.md)
  A publisher created by applying the zip function to three upstream publishers.
- [Publishers.Zip4](./zip4.md)
  A publisher created by applying the zip function to four upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip)*