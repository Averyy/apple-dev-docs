# collectionListType

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The type of asset collection group that the collection list represents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var collectionListType: PHCollectionListType { get }
```

```objc
@property (nonatomic, assign, readonly) PHCollectionListType collectionListType;
```

## Discussion

A collection list may represent an upper level of the Moments hierarchy shown in the Photos app, a folder that contains albums, or a smart folder synced from a Mac. See [`PHCollectionListType`](../phcollectionlisttype.md).

## See Also

### Reading Collection List Metadata
- [enum PHCollectionListType](../phcollectionlisttype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListType`](./collectionlisttype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./fetchcollectionlists%28with,subtype,options%29.md) method.
- [var collectionListSubtype: PHCollectionListSubtype](./collectionlistsubtype.md)
  The type of asset collection grouping the collection list represents.
- [enum PHCollectionListSubtype](../phcollectionlistsubtype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListSubtype`](./collectionlistsubtype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./fetchcollectionlists%28with,subtype,options%29.md), [`fetchMomentLists(with:containingMoment:options:)`](./fetchmomentlists%28with,containingmoment,options%29.md), and [`fetchMomentLists(with:options:)`](./fetchmomentlists%28with,options%29.md) methods.
- [var startDate: Date?](./startdate.md)
  The earliest creation date among all assets in the collection list.
- [var endDate: Date?](./enddate.md)
  The latest creation date among all assets in the collection list.
- [var localizedLocationNames: [String]](./localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist/collectionlisttype)*