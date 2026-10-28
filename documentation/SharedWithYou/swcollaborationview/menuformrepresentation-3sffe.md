# menuFormRepresentation

**Framework**: Shared with You  
**Kind**: property  
**Role**: Instance Property

Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.

**Availability**:
- macOS 13.1+

## Declaration

```swift
@MainActor
@objc @preconcurrency dynamic var menuFormRepresentation: NSMenuItem { get }
```

## Discussion

If this [`SWCollaborationView`](../swcollaborationview.md) instance is being set on an [`NSToolbarItem`](../../AppKit/nstoolbaritem.md), assign this property to the item’s `menuFormRepresentation` property.

## See Also

### Accessing view attributes
- [var activeParticipantCount: Int](./activeparticipantcount.md)
  The number of participants in a collaboration.
- [var cloudSharingDelegate: (any UICloudSharingControllerDelegate)?](./cloudsharingdelegate.md)
  The delegate object for the cloud-sharing controller.
- [var delegate: (any SWCollaborationViewDelegate)?](./delegate.md)
  The delegate object for the collaboration view.
- [var headerImage: UIImage](./headerimage.md)
  The image that the system displays in the header.
- [var headerSubtitle: String](./headersubtitle.md)
  The subtitle that the system displays in the header.
- [var headerTitle: String](./headertitle.md)
  The title that the system displays in the header.
- [var manageButtonTitle: String](./managebuttontitle.md)
  The manage button title that the system displays in the header.
- [var menuFormRepresentation: NSMenuItem](./menuformrepresentation-55skx.md)
  Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/menuformrepresentation-3sffe)*