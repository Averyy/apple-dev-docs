# collectionListSubtype

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The type of asset collection grouping the collection list represents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var collectionListSubtype: PHCollectionListSubtype { get }
```

```objc
@property (nonatomic, assign, readonly) PHCollectionListSubtype collectionListSubtype;
```

## Discussion

Use subtypes to make minor distinctions between collection lists of the same type, such as moment clusters and moment years. See [`PHCollectionListSubtype`](../phcollectionlistsubtype.md).

## See Also

### Reading Collection List Metadata
- [var collectionListType: PHCollectionListType](./collectionlisttype.md)
  The type of asset collection group that the collection list represents.
- [enum PHCollectionListType](../phcollectionlisttype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListType`](./collectionlisttype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./fetchcollectionlists%28with,subtype,options%29.md) method.
- [enum PHCollectionListSubtype](../phcollectionlistsubtype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListSubtype`](./collectionlistsubtype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./fetchcollectionlists%28with,subtype,options%29.md), [`fetchMomentLists(with:containingMoment:options:)`](./fetchmomentlists%28with,containingmoment,options%29.md), and [`fetchMomentLists(with:options:)`](./fetchmomentlists%28with,options%29.md) methods.
- [var startDate: Date?](./startdate.md)
  The earliest creation date among all assets in the collection list.
- [var endDate: Date?](./enddate.md)
  The latest creation date among all assets in the collection list.
- [var localizedLocationNames: [String]](./localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist/collectionlistsubtype)*