# UILocalizedIndexedCollation

**Framework**: UIKit  
**Kind**: class

An object that organizes, sorts, and localizes the data for a table view that has a section index.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UILocalizedIndexedCollation
```

#### Overview

Use a [`UILocalizedIndexedCollation`](uilocalizedindexedcollation.md) object in conjunction with your table’s data source object to sort and manage the data in an indexed table view. An index is an ideal way for users to navigate a table view containing sequential content. For example, the Contacts app sorts contacts alphabetically and displays an index for navigating those contacts quickly. You use the collation object as the source of the table’s section titles and index titles in your table view. You also use it to sort items in each section of your table.

To prepare the data for a section index, create an indexed-collation object and call [`section(for:collationStringSelector:)`](uilocalizedindexedcollation/section(for:collationstringselector:).md) for each model object to be indexed. That method determines the section in which each of these objects should appear and returns an integer that identifies the section. The table-view controller then puts each object in a local array for its section. For each section array, the controller calls the [`sortedArray(from:collationStringSelector:)`](uilocalizedindexedcollation/sortedarray(from:collationstringselector:).md) method to sort all of the objects in the section. The indexed-collation object is now the data store that the table-view controller uses to provide section-index data to the table view, as shown in the following example code.

## Topics

### Getting the shared instance
- [class func current() -> Self](uilocalizedindexedcollation/current.md)
  Returns an indexed-collation instance for the current table view.
### Preparing the sections and section indexes
- [func section(for: Any, collationStringSelector: Selector) -> Int](uilocalizedindexedcollation/section(for:collationstringselector:).md)
  Returns an integer identifying the section in which a model object belongs.
- [func sortedArray(from: [Any], collationStringSelector: Selector) -> [Any]](uilocalizedindexedcollation/sortedarray(from:collationstringselector:).md)
  Sorts the objects within a section by their localized titles.
### Providing section index data to the table view
- [var sectionTitles: [String]](uilocalizedindexedcollation/sectiontitles.md)
  Returns the list of section titles for the table view.
- [var sectionIndexTitles: [String]](uilocalizedindexedcollation/sectionindextitles.md)
  Returns the list of section-index titles for the table view.
- [func section(forSectionIndexTitle: Int) -> Int](uilocalizedindexedcollation/section(forsectionindextitle:).md)
  Returns the section that the table view should scroll to for the given index title.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Filling a table with data](filling-a-table-with-data.md)
  Create and configure cells for your table dynamically using a data source object, or provide them statically from your storyboard.
- [Asynchronously loading images into table and collection views](asynchronously-loading-images-into-table-and-collection-views.md)
  Store and fetch images asynchronously to make your app more responsive.
- [protocol UITableViewDataSource](uitableviewdatasource.md)
  The methods that an object adopts to manage data and provide cells for a table view.
- [protocol UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.
- [class UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md)
  The object you use to manage data and provide cells for a table view.
- [struct NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md)
  A representation of the state of the data in a view at a specific point in time.
- [protocol UIDataSourceTranslating](uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation)*