# Publishers.Merge7

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher created by applying the merge function to seven upstream publishers.

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
struct Merge7<A, B, C, D, E, F, G> where A : Publisher, B : Publisher, C : Publisher, D : Publisher, E : Publisher, F : Publisher, G : Publisher, A.Failure == B.Failure, A.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output, C.Failure == D.Failure, C.Output == D.Output, D.Failure == E.Failure, D.Output == E.Output, E.Failure == F.Failure, E.Output == F.Output, F.Failure == G.Failure, F.Output == G.Output
```

## Topics

### Creating a merge-seven publisher
- [init(A, B, C, D, E, F, G)](./merge7/init%28_,_,_,_,_,_,_%29.md)
  Creates a publisher created by applying the merge function to seven upstream publishers.
### Merging elements
- [func merge<P>(with: P) -> Publishers.Merge8<A, B, C, D, E, F, G, P>](./merge7/merge%28with%29.md)
### Declaring supporting types
- [Publishers.Merge7.Output](./merge7/output.md)
  The kind of values published by this publisher.
- [Publishers.Merge7.Failure](./merge7/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](./merge7/a.md)
  A publisher to merge.
- [let b: B](./merge7/b.md)
  A second publisher to merge.
- [let c: C](./merge7/c.md)
  A third publisher to merge.
- [let d: D](./merge7/d.md)
  A fourth publisher to merge.
- [let e: E](./merge7/e.md)
  A fifth publisher to merge.
- [let f: F](./merge7/f.md)
  A sixth publisher to merge.
- [let g: G](./merge7/g.md)
  An seventh publisher to merge.
### Comparing publishers
- [static func == (Publishers.Merge7<A, B, C, D, E, F, G>, Publishers.Merge7<A, B, C, D, E, F, G>) -> Bool](./merge7/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./merge7/equatable-implementations.md)

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
- [Publishers.Merge8](./merge8.md)
  A publisher created by applying the merge function to eight upstream publishers.
- [Publishers.MergeMany](./mergemany.md)
  A publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [Publishers.Zip](./zip.md)
  A publisher created by applying the zip function to two upstream publishers.
- [Publishers.Zip3](./zip3.md)
  A publisher created by applying the zip function to three upstream publishers.
- [Publishers.Zip4](./zip4.md)
  A publisher created by applying the zip function to four upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge7)*