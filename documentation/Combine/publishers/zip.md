# Publishers.Zip

**Framework**: Combine  
**Kind**: struct

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

#### Overview

Use `Publishers.Zip` to combine the latest elements from two publishers and emit a tuple to the downstream. The returned publisher waits until both publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together as a tuple to the subscriber.

Much like a zipper or zip fastener on a piece of clothing pulls together rows of teeth to link the two sides, `Publishers.Zip` combines streams from two different publishers by linking pairs of elements from each side.

If either upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## Topics

### Creating a zip publisher
- [init(_:_:)](publishers/zip/init(_:_:).md)
  Creates a publisher that applies the zip function to two upstream publishers.
### Declaring supporting types
- [Publishers.Zip.Output](publishers/zip/output.md)
  The kind of values published by this publisher.
- [Publishers.Zip.Failure](publishers/zip/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](publishers/zip/a.md)
  A publisher to zip.
- [let b: B](publishers/zip/b.md)
  Another publisher to zip.
### Comparing publishers
- [static func == (Publishers.Zip<A, B>, Publishers.Zip<A, B>) -> Bool](publishers/zip/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](publishers/zip/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.CombineLatest](publishers/combinelatest.md)
  A publisher that receives and combines the latest elements from two publishers.
- [Publishers.CombineLatest3](publishers/combinelatest3.md)
  A publisher that receives and combines the latest elements from three publishers.
- [Publishers.CombineLatest4](publishers/combinelatest4.md)
  A publisher that receives and combines the latest elements from four publishers.
- [Publishers.Merge](publishers/merge.md)
  A publisher created by applying the merge function to two upstream publishers.
- [Publishers.Merge3](publishers/merge3.md)
  A publisher created by applying the merge function to three upstream publishers.
- [Publishers.Merge4](publishers/merge4.md)
  A publisher created by applying the merge function to four upstream publishers.
- [Publishers.Merge5](publishers/merge5.md)
  A publisher created by applying the merge function to five upstream publishers.
- [Publishers.Merge6](publishers/merge6.md)
  A publisher created by applying the merge function to six upstream publishers.
- [Publishers.Merge7](publishers/merge7.md)
  A publisher created by applying the merge function to seven upstream publishers.
- [Publishers.Merge8](publishers/merge8.md)
  A publisher created by applying the merge function to eight upstream publishers.
- [Publishers.MergeMany](publishers/mergemany.md)
  A publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [Publishers.Zip3](publishers/zip3.md)
  A publisher created by applying the zip function to three upstream publishers.
- [Publishers.Zip4](publishers/zip4.md)
  A publisher created by applying the zip function to four upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip)*