# sectionIndexTitles

**Framework**: UIKit  
**Kind**: property

Returns the list of section-index titles for the table view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sectionIndexTitles: [String] { get }
```

#### Discussion

This property contains the localized list of section-index titles sorted according to the specified ordering (for example, A through Z in US English). In its implementation of [`sectionIndexTitles(for:)`](uitableviewdatasource/sectionindextitles(for:).md), the data source can call this method on the indexed-collation object and pass back the result.

## See Also

- [var sectionTitles: [String]](uilocalizedindexedcollation/sectiontitles.md)
  Returns the list of section titles for the table view.
- [func section(forSectionIndexTitle: Int) -> Int](uilocalizedindexedcollation/section(forsectionindextitle:).md)
  Returns the section that the table view should scroll to for the given index title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/sectionindextitles)*