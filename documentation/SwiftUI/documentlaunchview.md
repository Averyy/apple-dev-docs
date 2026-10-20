# DocumentLaunchView

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A view to present when launching document-related user experience.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
nonisolated
struct DocumentLaunchView<Actions, DocumentView> where Actions : View, DocumentView : View
```

#### Overview

> ❗ **Important**: To create new documents, set [`UISupportsDocumentBrowser`](../BundleResources/information-property-list/uisupportsdocumentbrowser.md) to `YES` in your app’s information property list. Without this key, document creation doesn’t work.

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

> **Note**:  An alternative to `DocumentLaunchView` is a scene variant of this API: [`DocumentGroupLaunchScene`](./documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## Topics

### Creating a launch view with a background view
- [init(_:for:_:onDocumentOpen:)](./documentlaunchview/init%28_,for,_,ondocumentopen%29.md)
  Creates a view to present when launching document-related user experiences using a localized title and custom actions.
- [init(_:for:_:onDocumentOpen:background:)](./documentlaunchview/init%28_,for,_,ondocumentopen,background%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:)](./documentlaunchview/init%28_,for,_,ondocumentopen,background,backgroundaccessoryview%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and a background accessory view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:overlayAccessoryView:)](./documentlaunchview/init%28_,for,_,ondocumentopen,background,backgroundaccessoryview,overlayaccessoryview%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and accessory views.
- [init(_:for:_:onDocumentOpen:background:overlayAccessoryView:)](./documentlaunchview/init%28_,for,_,ondocumentopen,background,overlayaccessoryview%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and an overlay accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:)](./documentlaunchview/init%28_,for,_,ondocumentopen,backgroundaccessoryview%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)](./documentlaunchview/init%28_,for,_,ondocumentopen,backgroundaccessoryview,overlayaccessoryview%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and accessory views.
- [init(_:for:_:onDocumentOpen:overlayAccessoryView:)](./documentlaunchview/init%28_,for,_,ondocumentopen,overlayaccessoryview%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and an overlay accessory view.
### Creating a launch view with a background style
- [init(_:for:backgroundStyle:_:onDocumentOpen:)](./documentlaunchview/init%28_,for,backgroundstyle,_,ondocumentopen%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background style.
- [init(_:for:backgroundStyle:_:onDocumentOpen:backgroundAccessoryView:)](./documentlaunchview/init%28_,for,backgroundstyle,_,ondocumentopen,backgroundaccessoryview%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and a background accessory view.
- [init(_:for:backgroundStyle:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)](./documentlaunchview/init%28_,for,backgroundstyle,_,ondocumentopen,backgroundaccessoryview,overlayaccessoryview%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and accessory views.
- [init(_:for:backgroundStyle:_:onDocumentOpen:overlayAccessoryView:)](./documentlaunchview/init%28_,for,backgroundstyle,_,ondocumentopen,overlayaccessoryview%29.md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and an overlay accessory view.
### Displaying the launch view
- [var body: some View](./documentlaunchview/body.md)
  The body of the view.

## Relationships

### Conforms To
- [View](./view.md)

## See Also

### Configuring the document launch experience
- [struct DocumentGroupLaunchScene](./documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [func documentLaunchTitle(_:)](./scene/documentlaunchtitle%28_%29.md)
  Sets the title displayed on the document launch card.
- [func documentLaunchSubtitle(_:)](./scene/documentlaunchsubtitle%28_%29.md)
  Sets the subtitle displayed beneath the title on the document launch card.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentlaunchview)*