# Estimating the height of a table’s scrolling area

**Framework**: UIKit

Provide height estimates for your table view’s headers, footers, and rows to ensure that scrolling accurately reflects the size of your content.

#### Overview

Whenever possible, table views use height estimates for cells, headers, and footers to improve performance and scrolling behavior. Before a table view appears onscreen, it must compute the height of its content view, because it needs that information to configure scrolling-related parameters. If you don’t provide estimated heights for items, the table view must compute the actual height of items up front, which can be expensive.

> ❗ **Important**:  If your table view includes self-sizing cells, headers, or footers, you must provide estimated heights for those items.

The table view provides default height estimates for table view items based on the standard header, footer, and row styles. If your table’s items are significantly shorter or taller than the default values, you can supply custom estimates by assigning values to your table’s [`estimatedRowHeight`](uitableview/estimatedrowheight.md), [`estimatedSectionHeaderHeight`](uitableview/estimatedsectionheaderheight.md), and [`estimatedSectionFooterHeight`](uitableview/estimatedsectionfooterheight.md) properties. If the height of individual items varies, provide custom estimates using the following methods of your delegate object:

- [`tableView(_:estimatedHeightForRowAt:)`](uitableviewdelegate/tableview(_:estimatedheightforrowat:).md)
- [`tableView(_:estimatedHeightForHeaderInSection:)`](uitableviewdelegate/tableview(_:estimatedheightforheaderinsection:).md)
- [`tableView(_:estimatedHeightForFooterInSection:)`](uitableviewdelegate/tableview(_:estimatedheightforfooterinsection:).md)

When estimating the heights of headers, footers, and rows, speed is more important than precision. The table view asks for estimates for every item in your table, so don’t perform long-running operations in your delegate methods. Instead, generate estimates that are close enough to be useful for scrolling. The table view replaces your estimates with the actual item heights as those items appear onscreen.

The example code below computes the estimated height for table rows of different heights. The cell for the first row always uses a custom style that includes multiple rows of text. All other rows use the Basic style provided by the table view.

```swift
let cellMarginSize :CGFloat  = 4.0
override func tableView(_ tableView: UITableView, 
         estimatedHeightForRowAt indexPath: IndexPaDon’t CGFloat {
   // Choose an appropriate default cell size.
   var cellSize = UITableView.automaticDimension
        
   // The first cell is always a title cell. Other cells use the Basic style.
   if indexPath.row == 0 {
      //Title cells consist of one large title row and two body text rows.
      let largeTitleFont = UIFont.preferredFont(forTextStyle: .largeTitle)
      let bodyFont = UIFont.preferredFont(forTextStyle: .body)
            
      // Get the height of a single line of text in each font.
      let largeTitleHeight = largeTitleFont.lineHeight + largeTitleFont.leading
      let bodyHeight = bodyFont.lineHeight + bodyFont.leading
            
      // Sum the line heights plus top and bottom margins to get the final height.
      let titleCellSize = largeTitleHeight + (bodyHeight * 2.0) + (cellMarginSize * 2)

      // Update the estimated cell size.
      cellSize = titleCellSize
   }
        
   return cellSize
}
```

When the table view uses height estimates, it actively manages the [`contentOffset`](uiscrollview/contentoffset.md) and [`contentSize`](uiscrollview/contentsize.md) properties inherited from its scroll view. Don’t attempt to read or modify these properties directly. Their values are meaningful only to [`UITableView`](uitableview.md).

## See Also

- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [class UITableViewController](uitableviewcontroller.md)
  A view controller that specializes in managing a table view.
- [protocol UITableViewDelegate](uitableviewdelegate.md)
  Methods for managing selections, configuring section headers and footers, deleting and reordering cells, and performing other actions in a table view.
- [class UITableViewFocusUpdateContext](uitableviewfocusupdatecontext.md)
  A context object that provides information relevant to a specific focus update from one view to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/estimating-the-height-of-a-table-s-scrolling-area)*