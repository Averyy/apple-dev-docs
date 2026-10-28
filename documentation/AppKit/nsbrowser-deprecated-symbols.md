# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func column(of: NSMatrix) -> Int](./nsbrowser/column%28of%29.md)
  Returns the column number in which the given matrix is located.
- [func matrix(inColumn: Int) -> NSMatrix?](./nsbrowser/matrix%28incolumn%29.md)
  Returns the matrix located in the specified column.
- [func matrixClass() -> AnyClass](./nsbrowser/matrixclass%28%29.md)
  Returns the matrix class used in the browser’s columns.
- [func setMatrixClass(AnyClass)](./nsbrowser/setmatrixclass%28_%29.md)
  Sets the matrix class to be used in the browser’s columns.
- [- updateScroller](./nsbrowser/updatescroller.md)
  Updates the horizontal scroller to reflect column positions.
- [- scrollViaScroller:](./nsbrowser/scrollviascroller_.md)
  Scrolls columns left or right based on an `NSScroller`.
- [- displayAllColumns](./nsbrowser/displayallcolumns.md)
  Updates the browser to display all loaded columns.
- [- displayColumn:](./nsbrowser/displaycolumn_.md)
  Updates the browser to display the given column.
- [- acceptsArrowKeys](./nsbrowser/acceptsarrowkeys.md)
  Indicates whether the browser allows navigation using the arrow keys.
- [- setAcceptsArrowKeys:](./nsbrowser/setacceptsarrowkeys_.md)
  Specifies whether the browser allows navigation using the arrow keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser-deprecated-symbols)*