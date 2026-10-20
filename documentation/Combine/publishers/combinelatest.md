# Publishers.CombineLatest

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that receives and combines the latest elements from two publishers.

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
struct CombineLatest<A, B> where A : Publisher, B : Publisher, A.Failure == B.Failure
```

## Topics

### Creating a combine latest publisher
- [init(_:_:)](./combinelatest/init%28_,_%29.md)
  Creates a publisher that receives and combines the latest elements from two publishers.
### Declaring supporting types
- [Publishers.CombineLatest.Output](./combinelatest/output.md)
  The kind of values published by this publisher.
- [Publishers.CombineLatest.Failure](./combinelatest/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](./combinelatest/a.md)
- [let b: B](./combinelatest/b.md)
### Comparing publishers
- [static func == (Publishers.CombineLatest<A, B>, Publishers.CombineLatest<A, B>) -> Bool](./combinelatest/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./combinelatest/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Combining elements from multiple publishers
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
- [Publishers.Zip3](./zip3.md)
  A publisher created by applying the zip function to three upstream publishers.
- [Publishers.Zip4](./zip4.md)
  A publisher created by applying the zip function to four upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/combinelatest)*