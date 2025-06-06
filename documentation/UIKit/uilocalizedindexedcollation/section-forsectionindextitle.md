# section(forSectionIndexTitle:)

**Framework**: UIKit  
**Kind**: method

Returns the section that the table view should scroll to for the given index title.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func section(forSectionIndexTitle indexTitleIndex: Int) -> Int
```

#### Return Value

An integer identifying the table-view section associated with `indexTitleIndex`.

#### Discussion

This method allows the table view to map between a given item in the section index and a given section even when there isn’t a one-to-one mapping. In its implementation of [`tableView(_:sectionForSectionIndexTitle:at:)`](uitableviewdatasource/tableview(_:sectionforsectionindextitle:at:).md), the data source can call this method on the indexed-collation object specifying as an argument the passed-in index integer; it then returns the result to the table view.

## Parameters

- `indexTitleIndex`: An integer identifying a section-index title by its position in the array of such titles.

## See Also

- [var sectionTitles: [String]](uilocalizedindexedcollation/sectiontitles.md)
  Returns the list of section titles for the table view.
- [var sectionIndexTitles: [String]](uilocalizedindexedcollation/sectionindextitles.md)
  Returns the list of section-index titles for the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/section(forsectionindextitle:))*