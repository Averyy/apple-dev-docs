# sections

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The sections for the fetch results.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sections: [any NSFetchedResultsSectionInfo]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<id<NSFetchedResultsSectionInfo>> * sections;
```

#### Discussion

The objects in the sections array implement the [`NSFetchedResultsSectionInfo`](../nsfetchedresultssectioninfo.md) protocol.

You typically use the sections array when implementing `UITableViewDataSource` methods, such as [`numberOfSections(in:)`](../../UIKit/uitableviewdatasource/numberofsections%28in%29.md) and [`tableView(_:titleForHeaderInSection:)`](../../UIKit/uitableviewdatasource/tableview%28_,titleforheaderinsection%29.md).

## See Also

### Querying Section Information
- [func section(forSectionIndexTitle: String, at: Int) -> Int](./section%28forsectionindextitle,at%29.md)
  Returns the section number for a given section title and index in the section index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/sections)*