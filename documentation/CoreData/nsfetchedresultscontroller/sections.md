# sections

**Framework**: Core Data  
**Kind**: property

The sections for the fetch results.

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
var sections: [any NSFetchedResultsSectionInfo]? { get }
```

#### Discussion

The objects in the sections array implement the [`NSFetchedResultsSectionInfo`](nsfetchedresultssectioninfo.md) protocol.

You typically use the sections array when implementing `UITableViewDataSource` methods, such as [`numberOfSections(in:)`](https://developer.apple.com/documentation/UIKit/UITableViewDataSource/numberOfSections(in:)) and [`tableView(_:titleForHeaderInSection:)`](https://developer.apple.com/documentation/UIKit/UITableViewDataSource/tableView(_:titleForHeaderInSection:)).

## See Also

- [func section(forSectionIndexTitle: String, at: Int) -> Int](nsfetchedresultscontroller/section(forsectionindextitle:at:).md)
  Returns the section number for a given section title and index in the section index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/sections)*