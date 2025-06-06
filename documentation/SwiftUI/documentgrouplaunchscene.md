# DocumentGroupLaunchScene

**Framework**: SwiftUI  
**Kind**: struct

A launch scene for document-based applications.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DocumentGroupLaunchScene<Actions> where Actions : View
```

#### Overview

You can use this launch scene alongside [`DocumentGroup`](documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [`DocumentLaunchView`](documentlaunchview.md).

If you don’t provide the title of the scene, it displays the application name. If you don’t provide the actions builder, the scene has the default “Create Document” action that creates new documents. To customize the document launch experience, you can replace the standard screen background and title, add decorative views, and add custom actions.

A `DocumentGroupLaunchScene` configures the document browser on the bottom sheet to open content types from all the document groups in the app definition. A `DocumentGroupLaunchScene` also configures the document groups to create documents of the first content type that your application can create and write.

For more information, see `FileDocument.writableContentTypes` and `ReferenceFileDocument.writableContentTypes`.

## Topics

### Initializers
- [init(_:_:background:)](documentgrouplaunchscene/init(_:_:background:).md)
  Creates a launch scene for document-based applications with a title, a set of actions, and a background.
- [init(_:_:background:backgroundAccessoryView:)](documentgrouplaunchscene/init(_:_:background:backgroundaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a set of actions, a background, and a background accessory view.
- [init(_:_:background:backgroundAccessoryView:overlayAccessoryView:)](documentgrouplaunchscene/init(_:_:background:backgroundaccessoryview:overlayaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a set of actions, and a background.
- [init(_:_:background:overlayAccessoryView:)](documentgrouplaunchscene/init(_:_:background:overlayaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a set of actions, a background, and an overlay accessory view.
- [init(_:backgroundStyle:_:)](documentgrouplaunchscene/init(_:backgroundstyle:_:).md)
  Creates a launch scene for document-based applications with a title, a background style, and a set of actions.
- [init(_:backgroundStyle:_:backgroundAccessoryView:)](documentgrouplaunchscene/init(_:backgroundstyle:_:backgroundaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and a background accessory view.
- [init(_:backgroundStyle:_:backgroundAccessoryView:overlayAccessoryView:)](documentgrouplaunchscene/init(_:backgroundstyle:_:backgroundaccessoryview:overlayaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and background and overlay accessory views.
- [init(_:backgroundStyle:_:overlayAccessoryView:)](documentgrouplaunchscene/init(_:backgroundstyle:_:overlayaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and an overlay accessory view.

## Relationships

### Conforms To
- [Scene](scene.md)

## See Also

- [struct DocumentLaunchView](documentlaunchview.md)
  A view to present when launching document-related user experience.
- [struct DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [struct NewDocumentButton](newdocumentbutton.md)
  A button that creates and opens new documents.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene)*