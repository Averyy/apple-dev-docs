# documentLaunchSubtitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the subtitle displayed beneath the title on the document launch card.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
nonisolated
func documentLaunchSubtitle(_ subtitle: Text) -> some Scene
```

**Other overloads**:

```swift
nonisolated
func documentLaunchSubtitle(_ subtitleKey: LocalizedStringKey) -> some Scene
```

```swift
nonisolated
func documentLaunchSubtitle(_ subtitleResource: LocalizedStringResource) -> some Scene
```

```swift
nonisolated
func documentLaunchSubtitle<S>(_ subtitle: S) -> some Scene where S : StringProtocol
```

## Discussion

Use this modifier to add descriptive text beneath the launch card title. Apply the modifier to a [`DocumentGroupLaunchScene`](../documentgrouplaunchscene.md) or any of its ancestors.

## Parameters

- `subtitle`: The subtitle to display.

## See Also

### Configuring the document launch experience
- [struct DocumentGroupLaunchScene](../documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [func documentLaunchTitle(_:)](./documentlaunchtitle%28_%29.md)
  Sets the title displayed on the document launch card.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/documentlaunchsubtitle(_:))*