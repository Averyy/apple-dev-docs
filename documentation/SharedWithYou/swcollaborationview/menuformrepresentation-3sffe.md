# menuFormRepresentation

**Framework**: Shared With You  
**Kind**: property

Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.

**Availability**:
- macOS 13.1+

## Declaration

```swift
@MainActor
@objc @preconcurrency dynamic var menuFormRepresentation: NSMenuItem { get }
```

#### Discussion

If this [`SWCollaborationView`](swcollaborationview.md) instance is being set on an [`NSToolbarItem`](https://developer.apple.com/documentation/AppKit/NSToolbarItem), assign this property to the item’s `menuFormRepresentation` property.

## See Also

- [var activeParticipantCount: Int](swcollaborationview/activeparticipantcount.md)
  The number of participants in a collaboration.
- [var cloudSharingDelegate: (any UICloudSharingControllerDelegate)?](swcollaborationview/cloudsharingdelegate.md)
  The delegate object for the cloud-sharing controller.
- [var delegate: (any SWCollaborationViewDelegate)?](swcollaborationview/delegate.md)
  The delegate object for the collaboration view.
- [var headerImage: UIImage](swcollaborationview/headerimage.md)
  The image that the system displays in the header.
- [var headerSubtitle: String](swcollaborationview/headersubtitle.md)
  The subtitle that the system displays in the header.
- [var headerTitle: String](swcollaborationview/headertitle.md)
  The title that the system displays in the header.
- [var manageButtonTitle: String](swcollaborationview/managebuttontitle.md)
  The manage button title that the system displays in the header.
- [var menuFormRepresentation: NSMenuItem](swcollaborationview/menuformrepresentation-55skx.md)
  Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/menuformrepresentation-3sffe)*