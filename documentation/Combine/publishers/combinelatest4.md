# Publishers.CombineLatest4

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that receives and combines the latest elements from four publishers.

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
struct CombineLatest4<A, B, C, D> where A : Publisher, B : Publisher, C : Publisher, D : Publisher, A.Failure == B.Failure, B.Failure == C.Failure, C.Failure == D.Failure
```

## Topics

### Creating a combine latest-four publisher
- [init(A, B, C, D)](./combinelatest4/init%28_,_,_,_%29.md)
### Declaring supporting types
- [Publishers.CombineLatest4.Output](./combinelatest4/output.md)
  The kind of values published by this publisher.
- [Publishers.CombineLatest4.Failure](./combinelatest4/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let a: A](./combinelatest4/a.md)
- [let b: B](./combinelatest4/b.md)
- [let c: C](./combinelatest4/c.md)
- [let d: D](./combinelatest4/d.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/combinelatest4)*