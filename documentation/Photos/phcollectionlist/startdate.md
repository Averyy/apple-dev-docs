# startDate

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The earliest creation date among all assets in the collection list.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var startDate: Date? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSDate * startDate;
```

#### Discussion

This property applies only to collection lists whose type is [`PHCollectionListType.momentList`](../phcollectionlisttype/momentlist.md). For other collection list types, this property’s value is `nil`.

## See Also

### Reading Collection List Metadata
- [var collectionListType: PHCollectionListType](./collectionlisttype.md)
  The type of asset collection group that the collection list represents.
- [enum PHCollectionListType](../phcollectionlisttype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListType`](./collectionlisttype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./fetchcollectionlists%28with,subtype,options%29.md) method.
- [var collectionListSubtype: PHCollectionListSubtype](./collectionlistsubtype.md)
  The type of asset collection grouping the collection list represents.
- [enum PHCollectionListSubtype](../phcollectionlistsubtype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListSubtype`](./collectionlistsubtype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./fetchcollectionlists%28with,subtype,options%29.md), [`fetchMomentLists(with:containingMoment:options:)`](./fetchmomentlists%28with,containingmoment,options%29.md), and [`fetchMomentLists(with:options:)`](./fetchmomentlists%28with,options%29.md) methods.
- [var endDate: Date?](./enddate.md)
  The latest creation date among all assets in the collection list.
- [var localizedLocationNames: [String]](./localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist/startdate)*