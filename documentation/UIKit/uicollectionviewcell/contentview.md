# contentView

**Framework**: UIKit  
**Kind**: property

The main view that you add your cell’s custom content to.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentView: UIView { get }
```

#### Discussion

When configuring a cell, you add any custom views representing your cell’s content to this view. The cell object places the content in this view in front of any background views.

## See Also

- [var contentConfiguration: (any UIContentConfiguration)?](uicollectionviewcell/contentconfiguration-13e7k.md)
  The current content configuration of the cell.
- [var automaticallyUpdatesContentConfiguration: Bool](uicollectionviewcell/automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/contentview)*