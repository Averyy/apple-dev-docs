# PHCollectionListSubtype

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Major distinctions between kinds of collection list, used by the [`collectionListSubtype`](./phcollectionlist/collectionlistsubtype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./phcollectionlist/fetchcollectionlists%28with,subtype,options%29.md), [`fetchMomentLists(with:containingMoment:options:)`](./phcollectionlist/fetchmomentlists%28with,containingmoment,options%29.md), and [`fetchMomentLists(with:options:)`](./phcollectionlist/fetchmomentlists%28with,options%29.md) methods.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHCollectionListSubtype
```

```c
enum PHCollectionListSubtype : NSInteger;
```

## Topics

### Constants
- [PHCollectionListSubtype.momentListCluster](./phcollectionlistsubtype/momentlistcluster.md)
  The collection list is a moment cluster, grouping several related moments.
- [PHCollectionListSubtype.momentListYear](./phcollectionlistsubtype/momentlistyear.md)
  The collection list is a moment year, grouping all moments from one or more calendar years.
- [PHCollectionListSubtype.regularFolder](./phcollectionlistsubtype/regularfolder.md)
  The collection list is a folder containing albums or other folders.
- [PHCollectionListSubtype.rootFolder](./phcollectionlistsubtype/rootfolder.md)
  The collection list that contains the top-level user collections.
- [PHCollectionListSubtype.smartFolderEvents](./phcollectionlistsubtype/smartfolderevents.md)
  The collection list is a smart folder containing one or more Events synced from a Mac.
- [PHCollectionListSubtype.smartFolderFaces](./phcollectionlistsubtype/smartfolderfaces.md)
  The collection list is a smart folder containing one or more Faces groups synced from a Mac.
- [PHCollectionListSubtype.any](./phcollectionlistsubtype/any.md)
  Use this value to fetch collection lists of all possible subtypes.
### Initializers
- [init?(rawValue: Int)](./phcollectionlistsubtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Reading Collection List Metadata
- [var collectionListType: PHCollectionListType](./phcollectionlist/collectionlisttype.md)
  The type of asset collection group that the collection list represents.
- [enum PHCollectionListType](./phcollectionlisttype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListType`](./phcollectionlist/collectionlisttype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./phcollectionlist/fetchcollectionlists%28with,subtype,options%29.md) method.
- [var collectionListSubtype: PHCollectionListSubtype](./phcollectionlist/collectionlistsubtype.md)
  The type of asset collection grouping the collection list represents.
- [var startDate: Date?](./phcollectionlist/startdate.md)
  The earliest creation date among all assets in the collection list.
- [var endDate: Date?](./phcollectionlist/enddate.md)
  The latest creation date among all assets in the collection list.
- [var localizedLocationNames: [String]](./phcollectionlist/localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistsubtype)*