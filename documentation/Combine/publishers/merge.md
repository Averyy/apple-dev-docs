# Publishers.Merge

**Framework**: Combine  
**Kind**: struct

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

### Creating a Merge Publisher
- [init(_:_:)](publishers/merge/init(_:_:).md)
  Creates a publisher created by applying the merge function to two upstream publishers.
### Declaring Publisher Topography
- [Publishers.Merge.Output](publishers/merge/output.md)
  The kind of values published by this publisher.
- [Publishers.Merge.Failure](publishers/merge/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let a: A](publishers/merge/a.md)
  A publisher to merge.
- [let b: B](publishers/merge/b.md)
  A second publisher to merge.
### Comparing Publishers
- [static func == (Publishers.Merge<A, B>, Publishers.Merge<A, B>) -> Bool](publishers/merge/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](publishers/merge/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](publishers-merge-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](publishers/merge/equatable-implementations.md)
- [Publisher Implementations](publishers/merge/publisher-implementations.md)

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
- [Publishers.Zip4](publishers/zip4.md)
  A publisher created by applying the zip function to four upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge)*