# NSFetchedResultsSectionInfo

**Framework**: Core Data  
**Kind**: protocol

A protocol that defines the interface for section objects vended by a fetched results controller.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol NSFetchedResultsSectionInfo
```

## Topics

### Accessing Objects
- [var numberOfObjects: Int](nsfetchedresultssectioninfo/numberofobjects.md)
  The number of objects (rows) in the section.
- [var objects: [Any]?](nsfetchedresultssectioninfo/objects.md)
  The array of objects in the section.
### Accessing the Name and Title
- [var name: String](nsfetchedresultssectioninfo/name.md)
  The name of the section.
- [var indexTitle: String?](nsfetchedresultssectioninfo/indextitle.md)
  The index title of the section.

## See Also

- [protocol NSFetchedResultsControllerDelegate](nsfetchedresultscontrollerdelegate.md)
  A delegate protocol that describes the methods that the associated fetched results controller calls when the fetch results change.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.
- [enum NSFetchedResultsChangeType](nsfetchedresultschangetype.md)
  Constants that specify the possible types of changes that are reported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultssectioninfo)*