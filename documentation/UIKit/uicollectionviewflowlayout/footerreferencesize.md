# footerReferenceSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The default sizes to use for section footers.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var footerReferenceSize: CGSize { get set }
```

```objc
@property (nonatomic) CGSize footerReferenceSize;
```

## Discussion

If the delegate does not implement the [`collectionView(_:layout:referenceSizeForFooterInSection:)`](../uicollectionviewdelegateflowlayout/collectionview%28_,layout,referencesizeforfooterinsection%29.md) method, the flow layout object uses the default footer sizes set for this property.

During layout, only the size that corresponds to the appropriate scrolling direction is used. For example, for the vertical scrolling direction, the layout object uses the height value specified by this property. (In that instance, the width of the footer would be set to the width of the collection view.) If the size in the appropriate scrolling dimension is 0, no footer is added.

The default size values are (0, 0).

## See Also

### Related Documentation
- [var sectionInset: UIEdgeInsets](./sectioninset.md)
  The margins used to lay out content in a section.
### Configuring headers and footers
- [var headerReferenceSize: CGSize](./headerreferencesize.md)
  The default sizes to use for section headers.
- [Flow layout supplementary views](../flow-layout-supplementary-views.md)
  Constants that specify the types of supplementary views that can be presented using a flow layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/footerreferencesize)*