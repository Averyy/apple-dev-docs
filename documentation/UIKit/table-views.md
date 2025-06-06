# Table views

**Framework**: UIKit

Display data in a single column of customizable rows.

#### Overview

A table view displays a single column of vertically scrolling content, divided into rows and sections. Each row of a table displays a single piece of information related to your app. Sections let you group related rows together. For example, the Contacts app uses a table to display the names of the user’s contacts.

![Illustration showing three table view examples. The first contains only rows, the second contains rows grouped into sections, and the third contains custom cells.](https://docs-assets.developer.apple.com/published/a62f6812cd9c5880d56e7f8ae8cb859c/media-3148899%402x.png)

Table views are a collaboration between many different objects, including:

- Cells. A cell provides the visual representation for your content. You can use the default cells provided by UIKit or define custom cells to suit the needs of your app.
- Table view controller. You typically use a [`UITableViewController`](uitableviewcontroller.md) object to manage a table view. You can use other view controllers too, but a table view controller is required for some table-related features to work.
- Your data source object. This object adopts the [`UITableViewDataSource`](uitableviewdatasource.md) protocol and provides the data for the table.
- Your delegate object. This object adopts the [`UITableViewDelegate`](uitableviewdelegate.md) protocol and manages user interactions with the table’s contents.

## Topics

### Essentials
- [class UITableView](uitableview.md)
  A view that presents data using rows in a single column.
### Data
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
- [class UILocalizedIndexedCollation](uilocalizedindexedcollation.md)
  An object that organizes, sorts, and localizes the data for a table view that has a section index.
- [protocol UIDataSourceTranslating](uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.
### Table management
- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md)
  Provide height estimates for your table view’s headers, footers, and rows to ensure that scrolling accurately reflects the size of your content.
- [class UITableViewController](uitableviewcontroller.md)
  A view controller that specializes in managing a table view.
- [protocol UITableViewDelegate](uitableviewdelegate.md)
  Methods for managing selections, configuring section headers and footers, deleting and reordering cells, and performing other actions in a table view.
- [class UITableViewFocusUpdateContext](uitableviewfocusupdatecontext.md)
  A context object that provides information relevant to a specific focus update from one view to another.
### Cells, headers, and footers
- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)
  Specify the appearance and content of your table’s rows by defining one or more prototype cells in your storyboard.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)
  Differentiate groups of rows visually by adding header and footer views to your table view’s sections.
- [class UITableViewCell](uitableviewcell.md)
  The visual representation of a single row in a table view.
- [class UITableViewHeaderFooterView](uitableviewheaderfooterview.md)
  A reusable view that you place at the top or bottom of a table section to display additional information for that section.
### Row actions
- [class UISwipeActionsConfiguration](uiswipeactionsconfiguration.md)
  The set of actions to perform when swiping on rows of a table.
- [class UIContextualAction](uicontextualaction.md)
  An action to display when the user swipes a table row.
- [class UITableViewRowAction](uitableviewrowaction.md)
  A single action to present when the user swipes horizontally in a table row.
### Selection management
- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)
  Detect when a user taps a table view cell so your app can take the next indicated action.
- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md)
  Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
### Drag and drop
- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)
  Initiate drags and handle drops from a table view.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md)
  Demonstrates how to enable and implement drag and drop for a table view.
- [protocol UITableViewDragDelegate](uitableviewdragdelegate.md)
  The interface for initiating drags from a table view.
- [protocol UITableViewDropDelegate](uitableviewdropdelegate.md)
  The interface for handling drops in a table view.
- [protocol UITableViewDropCoordinator](uitableviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the table view.
- [protocol UITableViewDropItem](uitableviewdropitem.md)
  The data associated with an item being dropped into the table view.
- [class UITableViewDropProposal](uitableviewdropproposal.md)
  Your proposed solution for handling a drop in a table view.
### Placeholder cells
- [protocol UITableViewDropPlaceholderContext](uitableviewdropplaceholdercontext.md)
  An object for tracking a placeholder cell that you added to your table during a drop operation.
- [class UITableViewDropPlaceholder](uitableviewdropplaceholder.md)
  A placeholder cell that supports customizing the drop preview parameters.
- [class UITableViewPlaceholder](uitableviewplaceholder.md)
  An object that contains information about a placeholder cell being inserted into a table.

## See Also

- [Autosizing Views for Localization in iOS](../xcode/autosizing_views_for_localization_in_ios.md)
  Add auto layout constraints to your app to achieve localizable views.
- [Collection views](collection-views.md)
  Display nested views using a configurable and highly customizable layout.
- [class UIStackView](uistackview.md)
  A streamlined interface for laying out a collection of views in either a column or a row.
- [class UIScrollView](uiscrollview.md)
  A view that allows the scrolling and zooming of its contained views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/table-views)*