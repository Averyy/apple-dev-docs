# Publishers.Merge4

**Framework**: Combine  
**Kind**: struct

A publisher created by applying the merge function to four upstream publishers.

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
struct Merge4<A, B, C, D> where A : Publisher, B : Publisher, C : Publisher, D : Publisher, A.Failure == B.Failure, A.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output, C.Failure == D.Failure, C.Output == D.Output
```

## Topics

### Creating a merge-four publisher
- [init(A, B, C, D)](publishers/merge4/init(_:_:_:_:).md)
  Creates a publisher created by applying the merge function to four upstream publishers.
### Merging elements
- [func merge<P>(with: P) -> Publishers.Merge5<A, B, C, D, P>](publishers/merge4/merge(with:).md)
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge6<A, B, C, D, Z, Y>](publishers/merge4/merge(with:_:).md)
- [func merge<Z, Y, X>(with: Z, Y, X) -> Publishers.Merge7<A, B, C, D, Z, Y, X>](publishers/merge4/merge(with:_:_:).md)
- [func merge<Z, Y, X, W>(with: Z, Y, X, W) -> Publishers.Merge8<A, B, C, D, Z, Y, X, W>](publishers/merge4/merge(with:_:_:_:).md)
### Declaring supporting types
- [Publishers.Merge4.Output](publishers/merge4/output.md)
  The kind of values published by this publisher.
- [Publishers.Merge4.Failure](publishers/merge4/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](publishers/merge4/a.md)
  A publisher to merge.
- [let b: B](publishers/merge4/b.md)
  A second publisher to merge.
- [let c: C](publishers/merge4/c.md)
  A third publisher to merge.
- [let d: D](publishers/merge4/d.md)
  A fourth publisher to merge.
### Comparing publishers
- [static func == (Publishers.Merge4<A, B, C, D>, Publishers.Merge4<A, B, C, D>) -> Bool](publishers/merge4/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](publishers/merge4/equatable-implementations.md)

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
- [Publishers.Zip4](publishers/zip4.md)
  A publisher created by applying the zip function to four upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge4)*