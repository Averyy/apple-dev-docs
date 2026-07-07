# documentLaunchSubtitle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the subtitle displayed beneath the title on the document launch card.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
nonisolated
func documentLaunchSubtitle(_ subtitle: Text) -> some Scene
```

#### Discussion

Use this modifier to add descriptive text beneath the launch card title. Apply the modifier to a [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md) or any of its ancestors.

## Parameters

- `subtitle`: The subtitle to display.

## See Also

- [struct DocumentGroupLaunchScene](documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [func documentLaunchTitle(_:)](scene/documentlaunchtitle(_:).md)
  Sets the title displayed on the document launch card.
- [struct DocumentLaunchView](documentlaunchview.md)
  A view to present when launching document-related user experience.
- [func documentLaunchTitle(_:)](view/documentlaunchtitle(_:).md)
  Sets the title displayed on the document launch card.
- [func documentLaunchSubtitle(_:)](view/documentlaunchsubtitle(_:).md)
  Sets the subtitle displayed beneath the title on the document launch card.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](view/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [struct DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [struct NewDocumentButton](newdocumentbutton.md)
  A button that creates and opens new documents.
- [struct DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md)
  The default label used for a new document button.
- [struct DocumentCreationSource](documentcreationsource.md)
  Describes the source used to create a new document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/documentlaunchsubtitle(_:))*