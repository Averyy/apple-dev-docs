# sectionTitles

**Framework**: UIKit  
**Kind**: property

Returns the list of section titles for the table view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sectionTitles: [String] { get }
```

#### Discussion

This property contains the localized list of section titles sorted according to the specified ordering (for example, A through Z in US English). In its implementation of [`tableView(_:titleForHeaderInSection:)`](uitableviewdatasource/tableview(_:titleforheaderinsection:).md), the data source can call this method on the indexed-collation object, passing in the section index and returning the result.

## See Also

- [var sectionIndexTitles: [String]](uilocalizedindexedcollation/sectionindextitles.md)
  Returns the list of section-index titles for the table view.
- [func section(forSectionIndexTitle: Int) -> Int](uilocalizedindexedcollation/section(forsectionindextitle:).md)
  Returns the section that the table view should scroll to for the given index title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/sectiontitles)*