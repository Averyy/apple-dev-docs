# cloudSharingDelegate

**Framework**: Shared with You  
**Kind**: property  
**Role**: Instance Property

The delegate object for the cloud-sharing controller.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
weak var cloudSharingDelegate: (any UICloudSharingControllerDelegate)? { get set }
```

*macOS*

```swift
weak var cloudSharingDelegate: (any NSCloudSharingServiceDelegate)? { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@property (nonatomic, weak) id<UICloudSharingControllerDelegate> cloudSharingDelegate;
```

*macOS*

```objc
@property (weak, nullable) id<NSCloudSharingServiceDelegate> cloudSharingDelegate;
```

## See Also

### Accessing view attributes
- [var activeParticipantCount: Int](./activeparticipantcount.md)
  The number of participants in a collaboration.
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
- [var menuFormRepresentation: NSMenuItem](./menuformrepresentation-3sffe.md)
  Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.
- [var menuFormRepresentation: NSMenuItem](./menuformrepresentation-55skx.md)
  Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/cloudsharingdelegate)*