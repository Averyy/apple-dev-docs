# DocumentGroupLaunchScene

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A launch scene for document-based applications.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
struct DocumentGroupLaunchScene<Actions> where Actions : View
```

#### Overview

You can use this launch scene alongside [`DocumentGroup`](./documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [`DocumentLaunchView`](./documentlaunchview.md).

If you don’t provide the title of the scene, it displays the application name. If you don’t provide the actions builder, the scene has the default “Create Document” action that creates new documents. To customize the document launch experience, you can replace the standard screen background and title, add decorative views, and add custom actions.

A `DocumentGroupLaunchScene` configures the document browser on the bottom sheet to open content types from all the document groups in the app definition. A `DocumentGroupLaunchScene` also configures the document groups to create documents of the first content type that your application can create and write.

If you provide one or two actions, each one appears as its own button. If you provide more than two actions, only the first action appears as a button; SwiftUI groups the remaining actions into a secondary “More” menu. Because people can’t create a new document from within that menu, place [`NewDocumentButton`](./newdocumentbutton.md) as the first action, or as the second action only when you provide exactly two actions in total. Use [`Button`](./button.md) for any actions beyond the first two.

For more information, see `FileDocument.writableContentTypes` and `ReferenceFileDocument.writableContentTypes`.

## Topics

### Creating a launch scene with a background view
- [init(_:_:background:)](./documentgrouplaunchscene/init%28_,_,background%29.md)
  Creates a launch scene for document-based applications with a title, a set of actions, and a background.
- [init(_:_:background:backgroundAccessoryView:)](./documentgrouplaunchscene/init%28_,_,background,backgroundaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a set of actions, a background, and a background accessory view.
- [init(_:_:background:backgroundAccessoryView:overlayAccessoryView:)](./documentgrouplaunchscene/init%28_,_,background,backgroundaccessoryview,overlayaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a set of actions, and a background.
- [init(_:_:background:overlayAccessoryView:)](./documentgrouplaunchscene/init%28_,_,background,overlayaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a set of actions, a background, and an overlay accessory view.
### Creating a launch scene with a background style
- [init(_:backgroundStyle:_:)](./documentgrouplaunchscene/init%28_,backgroundstyle,_%29.md)
  Creates a launch scene for document-based applications with a title, a background style, and a set of actions.
- [init(_:backgroundStyle:_:backgroundAccessoryView:)](./documentgrouplaunchscene/init%28_,backgroundstyle,_,backgroundaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and a background accessory view.
- [init(_:backgroundStyle:_:backgroundAccessoryView:overlayAccessoryView:)](./documentgrouplaunchscene/init%28_,backgroundstyle,_,backgroundaccessoryview,overlayaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and background and overlay accessory views.
- [init(_:backgroundStyle:_:overlayAccessoryView:)](./documentgrouplaunchscene/init%28_,backgroundstyle,_,overlayaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and an overlay accessory view.

## Relationships

### Conforms To
- [Scene](./scene.md)

## See Also

### Configuring the document launch experience
- [func documentLaunchTitle(_:)](./scene/documentlaunchtitle%28_%29.md)
  Sets the title displayed on the document launch card.
- [func documentLaunchSubtitle(_:)](./scene/documentlaunchsubtitle%28_%29.md)
  Sets the subtitle displayed beneath the title on the document launch card.
- [struct DocumentLaunchView](./documentlaunchview.md)
  A view to present when launching document-related user experience.
- [func documentLaunchTitle(_:)](./view/documentlaunchtitle%28_%29.md)
  Sets the title displayed on the document launch card.
- [func documentLaunchSubtitle(_:)](./view/documentlaunchsubtitle%28_%29.md)
  Sets the subtitle displayed beneath the title on the document launch card.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](./view/documentbrowsercontextmenu%28_%29.md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [struct DocumentLaunchGeometryProxy](./documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](./defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [struct NewDocumentButton](./newdocumentbutton.md)
  A button that creates and opens new documents.
- [struct DefaultNewDocumentButtonLabel](./defaultnewdocumentbuttonlabel.md)
  The default label used for a new document button.
- [struct DocumentCreationSource](./documentcreationsource.md)
  Describes the source used to create a new document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene)*