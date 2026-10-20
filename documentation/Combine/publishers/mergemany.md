# Publishers.MergeMany

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher created by applying the merge function to an arbitrary number of upstream publishers.

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
struct MergeMany<Upstream> where Upstream : Publisher
```

## Topics

### Creating a merge many publisher
- [init(Upstream...)](./mergemany/init%28_%29-1hsqd.md)
  Creates a publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [init<S>(S)](./mergemany/init%28_%29-3hrmo.md)
  Creates a publisher created by applying the merge function to a sequence of upstream publishers.
### Merging elements
- [func merge(with: Upstream) -> Publishers.MergeMany<Upstream>](./mergemany/merge%28with%29.md)
  Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
### Declaring supporting types
- [Publishers.MergeMany.Output](./mergemany/output.md)
  The kind of values published by this publisher.
- [Publishers.MergeMany.Failure](./mergemany/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let publishers: [Upstream]](./mergemany/publishers.md)
  The array of upstream publishers that this publisher merges together.
### Comparing publishers
- [static func == (Publishers.MergeMany<Upstream>, Publishers.MergeMany<Upstream>) -> Bool](./mergemany/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./mergemany/equatable-implementations.md)

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
- [Publishers.Zip](./zip.md)
  A publisher created by applying the zip function to two upstream publishers.
- [Publishers.Zip3](./zip3.md)
  A publisher created by applying the zip function to three upstream publishers.
- [Publishers.Zip4](./zip4.md)
  A publisher created by applying the zip function to four upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/mergemany)*