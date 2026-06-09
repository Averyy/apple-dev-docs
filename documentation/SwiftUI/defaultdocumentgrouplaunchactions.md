# DefaultDocumentGroupLaunchActions

**Framework**: SwiftUI  
**Kind**: struct

The default actions for the document group launch scene and the document launch view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
struct DefaultDocumentGroupLaunchActions
```

#### Overview

This `View` populates [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md) and [`DocumentLaunchView`](documentlaunchview.md) with the default actions.

## Topics

### Initializers
- [init()](defaultdocumentgrouplaunchactions/init.md)

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct DocumentGroupLaunchScene](documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [struct DocumentLaunchView](documentlaunchview.md)
  A view to present when launching document-related user experience.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](view/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [struct DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct NewDocumentButton](newdocumentbutton.md)
  A button that creates and opens new documents.
- [struct NewDocumentButtonDataSource](newdocumentbuttondatasource.md)
  Describes the source of data used to create a new document.
- [struct DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md)
  The default label used for a new document button.
- [struct DocumentCreationSource](documentcreationsource.md)
  Describes the source used to create a new document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/defaultdocumentgrouplaunchactions)*