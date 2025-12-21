# Publishers.Merge6

**Framework**: Combine  
**Kind**: struct

A publisher created by applying the merge function to six upstream publishers.

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
struct Merge6<A, B, C, D, E, F> where A : Publisher, B : Publisher, C : Publisher, D : Publisher, E : Publisher, F : Publisher, A.Failure == B.Failure, A.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output, C.Failure == D.Failure, C.Output == D.Output, D.Failure == E.Failure, D.Output == E.Output, E.Failure == F.Failure, E.Output == F.Output
```

## Topics

### Creating a merge-six publisher
- [init(A, B, C, D, E, F)](publishers/merge6/init(_:_:_:_:_:_:).md)
  publisher created by applying the merge function to six upstream publishers.
### Merging elements
- [func merge<P>(with: P) -> Publishers.Merge7<A, B, C, D, E, F, P>](publishers/merge6/merge(with:).md)
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge8<A, B, C, D, E, F, Z, Y>](publishers/merge6/merge(with:_:).md)
### Declaring supporting types
- [Publishers.Merge6.Output](publishers/merge6/output.md)
  The kind of values published by this publisher.
- [Publishers.Merge6.Failure](publishers/merge6/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](publishers/merge6/a.md)
  A publisher to merge.
- [let b: B](publishers/merge6/b.md)
  A second publisher to merge.
- [let c: C](publishers/merge6/c.md)
  A third publisher to merge.
- [let d: D](publishers/merge6/d.md)
  A fourth publisher to merge.
- [let e: E](publishers/merge6/e.md)
  A fifth publisher to merge.
- [let f: F](publishers/merge6/f.md)
  A sixth publisher to merge.
### Comparing publishers
- [static func == (Publishers.Merge6<A, B, C, D, E, F>, Publishers.Merge6<A, B, C, D, E, F>) -> Bool](publishers/merge6/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](publishers/merge6/equatable-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge6)*