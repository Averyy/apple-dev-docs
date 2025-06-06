# collectionView(_:layout:referenceSizeForHeaderInSection:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for the size of the header view in the specified section.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, layout collectionViewLayout: NSCollectionViewLayout, referenceSizeForHeaderInSection section: Int) -> NSSize
```

#### Return Value

The size of the header. Return [`NSZeroSize`](https://developer.apple.com/documentation/Foundation/NSZeroSize) if you do not want a header added to the section.

#### Discussion

If you implement this method, the flow layout object calls it to obtain the size of the header in each section and uses that information to set the size of the corresponding views. If you do not implement this method, the header size is obtained from the properties of the flow layout object.

The flow layout object uses only one of the returned size values. For a vertically scrolling layout, the layout object uses the height value. For a horizontally scrolling layout, the layout object uses the width value. The other value is sized appropriately to match the opposing dimension of the collection view itself. Set the size of the header to `0` to prevent it from being displayed.

## Parameters

- `collectionView`: The collection view object displaying the flow layout.
- `collectionViewLayout`: The layout object requesting the information.
- `section`: The index of the section whose header size is requested.

## See Also

- [var headerReferenceSize: NSSize](nscollectionviewflowlayout/headerreferencesize.md)
  The default size to use for section headers.
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, referenceSizeForFooterInSection: Int) -> NSSize](nscollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforfooterinsection:).md)
  Asks the delegate for the size of the footer view in the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforheaderinsection:))*