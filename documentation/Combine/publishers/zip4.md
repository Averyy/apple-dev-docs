# Publishers.Zip4

**Framework**: Combine  
**Kind**: struct

A publisher created by applying the zip function to four upstream publishers.

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
struct Zip4<A, B, C, D> where A : Publisher, B : Publisher, C : Publisher, D : Publisher, A.Failure == B.Failure, B.Failure == C.Failure, C.Failure == D.Failure
```

#### Overview

Use a `Publishers.Zip4` to combine the latest elements from four publishers and emit a tuple to the downstream. The returned publisher waits until all four publishers have emitted an event, then delivers the oldest unconsumed event from each publisher as a tuple to the subscriber.

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## Topics

### Creating a zip-four Publisher
- [init(A, B, C, D)](publishers/zip4/init(_:_:_:_:).md)
  Creates a publisher created by applying the zip function to four upstream publishers.
### Declaring supporting types
- [Publishers.Zip4.Output](publishers/zip4/output.md)
  The kind of values published by this publisher.
- [Publishers.Zip4.Failure](publishers/zip4/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](publishers/zip4/a.md)
  A publisher to zip.
- [let b: B](publishers/zip4/b.md)
  A second publisher to zip.
- [let c: C](publishers/zip4/c.md)
  A third publisher to zip.
- [let d: D](publishers/zip4/d.md)
  A fourth publisher to zip.
### Comparing publishers
- [static func == (Publishers.Zip4<A, B, C, D>, Publishers.Zip4<A, B, C, D>) -> Bool](publishers/zip4/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](publishers/zip4/equatable-implementations.md)

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
- [Publishers.Zip](publishers/zip.md)
  A publisher created by applying the zip function to two upstream publishers.
- [Publishers.Zip3](publishers/zip3.md)
  A publisher created by applying the zip function to three upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip4)*