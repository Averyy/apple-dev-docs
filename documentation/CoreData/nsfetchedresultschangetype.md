# NSFetchedResultsChangeType

**Framework**: Core Data  
**Kind**: enum

Constants that specify the possible types of changes that are reported.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum NSFetchedResultsChangeType
```

## Topics

### Constants
- [NSFetchedResultsChangeType.insert](nsfetchedresultschangetype/insert.md)
  Specifies that an object was inserted.
- [NSFetchedResultsChangeType.delete](nsfetchedresultschangetype/delete.md)
  Specifies that an object was deleted.
- [NSFetchedResultsChangeType.move](nsfetchedresultschangetype/move.md)
  Specifies that an object was moved.
- [NSFetchedResultsChangeType.update](nsfetchedresultschangetype/update.md)
  Specifies that an object was changed.
### Initializers
- [init?(rawValue: UInt)](nsfetchedresultschangetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NSFetchedResultsControllerDelegate](nsfetchedresultscontrollerdelegate.md)
  A delegate protocol that describes the methods that the associated fetched results controller calls when the fetch results change.
- [protocol NSFetchedResultsSectionInfo](nsfetchedresultssectioninfo.md)
  A protocol that defines the interface for section objects vended by a fetched results controller.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype)*