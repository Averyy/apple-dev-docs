# headerReferenceSize

**Framework**: UIKit  
**Kind**: property

The default sizes to use for section headers.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var headerReferenceSize: CGSize { get set }
```

#### Discussion

If the delegate does not implement the [`collectionView(_:layout:referenceSizeForHeaderInSection:)`](uicollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforheaderinsection:).md) method, the flow layout object uses the default header sizes set in this property.

During layout, only the size that corresponds to the appropriate scrolling direction is used. For example, for the vertical scrolling direction, the layout object uses the height value returned by your method. (In that instance, the width of the header would be set to the width of the collection view.) If the size in the appropriate scrolling dimension is 0, no header is added.

The default size values are (0, 0).

## See Also

- [var footerReferenceSize: CGSize](uicollectionviewflowlayout/footerreferencesize.md)
  The default sizes to use for section footers.
- [Flow layout supplementary views](flow-layout-supplementary-views.md)
  Constants that specify the types of supplementary views that can be presented using a flow layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/headerreferencesize)*