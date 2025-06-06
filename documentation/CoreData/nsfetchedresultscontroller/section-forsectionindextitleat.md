# section(forSectionIndexTitle:at:)

**Framework**: Core Data  
**Kind**: method

Returns the section number for a given section title and index in the section index.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func section(forSectionIndexTitle title: String, at sectionIndex: Int) -> Int
```

#### Return Value

The section number for the given section title and index in the section index

#### Discussion

You would typically call this method when executing `UITableViewDataSource`’s [`tableView(_:sectionForSectionIndexTitle:at:)`](https://developer.apple.com/documentation/UIKit/UITableViewDataSource/tableView(_:sectionForSectionIndexTitle:at:)) method.

## Parameters

- `title`: The title of a section
- `sectionIndex`: The index of a section.

## See Also

- [var sections: [any NSFetchedResultsSectionInfo]?](nsfetchedresultscontroller/sections.md)
  The sections for the fetch results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/section(forsectionindextitle:at:))*