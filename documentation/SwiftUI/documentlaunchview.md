# DocumentLaunchView

**Framework**: SwiftUI  
**Kind**: struct

A view to present when launching document-related user experience.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
nonisolated
struct DocumentLaunchView<Actions, DocumentView> where Actions : View, DocumentView : View
```

#### Overview

> ❗ **Important**: To create new documents, set [`UISupportsDocumentBrowser`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UISupportsDocumentBrowser) to `YES` in your app’s information property list. Without this key, document creation doesn’t work.

Configure `DocumentLaunchView` to open and display files and trigger custom actions.

For example, an application that offers writing books can present the `DocumentLaunchView` as its launch view:

```swift
public import UniformTypeIdentifiers

struct BookEditorLaunchView: View {

    var body: some View {
        DocumentLaunchView(for: [.book]) {
            NewDocumentButton("Start New Book")
        } onDocumentOpen: { url in
            BookEditor(url)
        }
    }
}

struct BookEditor: View {
    init(_ url: URL) { }
}

extension UTType {
    static let book = UTType(exportedAs: "com.example.bookEditor")
}
```

> **Note**:  An alternative to `DocumentLaunchView` is a scene variant of this API: [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## Topics

### Initializers
- [init(_:for:_:onDocumentOpen:)](documentlaunchview/init(_:for:_:ondocumentopen:).md)
  Creates a view to present when launching document-related user experiences using a localized title and custom actions.
- [init(_:for:_:onDocumentOpen:background:)](documentlaunchview/init(_:for:_:ondocumentopen:background:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:background:backgroundaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and a background accessory view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:overlayAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:background:backgroundaccessoryview:overlayaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and accessory views.
- [init(_:for:_:onDocumentOpen:background:overlayAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:background:overlayaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and an overlay accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:backgroundaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:backgroundaccessoryview:overlayaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and accessory views.
- [init(_:for:_:onDocumentOpen:overlayAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:overlayaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and an overlay accessory view.
- [init(_:for:backgroundStyle:_:onDocumentOpen:)](documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background style.
- [init(_:for:backgroundStyle:_:onDocumentOpen:backgroundAccessoryView:)](documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:backgroundaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and a background accessory view.
- [init(_:for:backgroundStyle:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)](documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:backgroundaccessoryview:overlayaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and accessory views.
- [init(_:for:backgroundStyle:_:onDocumentOpen:overlayAccessoryView:)](documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:overlayaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and an overlay accessory view.
### Instance Properties
- [var body: some View](documentlaunchview/body.md)
  The body of the view.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct DocumentGroupLaunchScene](documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](view/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [struct DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [struct NewDocumentButton](newdocumentbutton.md)
  A button that creates and opens new documents.
- [struct NewDocumentButtonDataSource](newdocumentbuttondatasource.md)
  Describes the source of data used to create a new document.
- [struct DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md)
  The default label used for a new document button.
- [struct DocumentCreationSource](documentcreationsource.md)
  Describes the source used to create a new document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentlaunchview)*