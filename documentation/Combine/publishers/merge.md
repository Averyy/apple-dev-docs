# Publishers.Merge

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher created by applying the merge function to two upstream publishers.

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
struct Merge<A, B> where A : Publisher, B : Publisher, A.Failure == B.Failure, A.Output == B.Output
```

## Topics

### Creating a merge publisher
- [init(_:_:)](./merge/init%28_,_%29.md)
  Creates a publisher created by applying the merge function to two upstream publishers.
### Merging elements
- [func merge<P>(with: P) -> Publishers.Merge3<A, B, P>](./merge/merge%28with%29.md)
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge4<A, B, Z, Y>](./merge/merge%28with,_%29.md)
- [func merge<Z, Y, X>(with: Z, Y, X) -> Publishers.Merge5<A, B, Z, Y, X>](./merge/merge%28with,_,_%29.md)
- [func merge<Z, Y, X, W>(with: Z, Y, X, W) -> Publishers.Merge6<A, B, Z, Y, X, W>](./merge/merge%28with,_,_,_%29.md)
- [func merge<Z, Y, X, W, V>(with: Z, Y, X, W, V) -> Publishers.Merge7<A, B, Z, Y, X, W, V>](./merge/merge%28with,_,_,_,_%29.md)
- [func merge<Z, Y, X, W, V, U>(with: Z, Y, X, W, V, U) -> Publishers.Merge8<A, B, Z, Y, X, W, V, U>](./merge/merge%28with,_,_,_,_,_%29.md)
### Declaring supporting types
- [Publishers.Merge.Output](./merge/output.md)
  The kind of values published by this publisher.
- [Publishers.Merge.Failure](./merge/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](./merge/a.md)
  A publisher to merge.
- [let b: B](./merge/b.md)
  A second publisher to merge.
### Comparing publishers
- [static func == (Publishers.Merge<A, B>, Publishers.Merge<A, B>) -> Bool](./merge/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./merge/equatable-implementations.md)

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
- [Publishers.Zip3](./zip3.md)
  A publisher created by applying the zip function to three upstream publishers.
- [Publishers.Zip4](./zip4.md)
  A publisher created by applying the zip function to four upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge)*