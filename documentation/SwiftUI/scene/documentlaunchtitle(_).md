# documentLaunchTitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the title displayed on the document launch card.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
nonisolated
func documentLaunchTitle(_ title: Text) -> some Scene
```

**Other overloads**:

```swift
nonisolated
func documentLaunchTitle(_ titleKey: LocalizedStringKey) -> some Scene
```

```swift
nonisolated
func documentLaunchTitle(_ titleResource: LocalizedStringResource) -> some Scene
```

```swift
nonisolated
func documentLaunchTitle<S>(_ title: S) -> some Scene where S : StringProtocol
```

## Discussion

Use this modifier to override the default launch-card title, which is the application name. Apply the modifier to a [`DocumentGroupLaunchScene`](../documentgrouplaunchscene.md) or any of its ancestors.

## Parameters

- `title`: The title to display.

## See Also

### Configuring the document launch experience
- [struct DocumentGroupLaunchScene](../documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [func documentLaunchSubtitle(_:)](./documentlaunchsubtitle%28_%29.md)
  Sets the subtitle displayed beneath the title on the document launch card.
- [struct DocumentLaunchView](../documentlaunchview.md)
  A view to present when launching document-related user experience.
- [func documentLaunchTitle(_:)](../view/documentlaunchtitle%28_%29.md)
  Sets the title displayed on the document launch card.
- [func documentLaunchSubtitle(_:)](../view/documentlaunchsubtitle%28_%29.md)
  Sets the subtitle displayed beneath the title on the document launch card.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](../view/documentbrowsercontextmenu%28_%29.md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [struct DocumentLaunchGeometryProxy](../documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](../defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [struct NewDocumentButton](../newdocumentbutton.md)
  A button that creates and opens new documents.
- [struct DefaultNewDocumentButtonLabel](../defaultnewdocumentbuttonlabel.md)
  The default label used for a new document button.
- [struct DocumentCreationSource](../documentcreationsource.md)
  Describes the source used to create a new document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/documentlaunchtitle(_:))*