# View coordination

**Framework**: BrowserEngineKit

Display content in the browser’s UI that an extension renders.

## Topics

### Layer hosting
- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)
  Coordinate view-hierarchy and layer-hierarchy changes between processes.
- [class LayerHierarchy](layerhierarchy.md)
  An object that holds a reference to layers rendered in another process’s view.
- [class LayerHierarchyHostingView](layerhierarchyhostingview.md)
  A view that hosts a layer hierarchy you manage in another process.
- [class LayerHierarchyHostingTransactionCoordinator](layerhierarchyhostingtransactioncoordinator.md)
  Synchronizes updates to views and layers in different processes.
- [class LayerHierarchyHandle](layerhierarchyhandle.md)
  A reference to a layer hierarchy that you share between processes.
### Visibility propagation
- [Propagating view visibility information to extension processes](propagating-view-visibility-information-to-browser-extensions.md)
  Register the extensions that contribute to preparing your browser app’s UI.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](renderingprocess/createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the rendering process.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](webcontentprocess/createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the web content process.

## See Also

- [Text interaction](text-interaction.md)
  Integrate your web browser engine asynchronously with the text system.
- [class BEWebAppManifest](bewebappmanifest.md)
  An object that represents a web app manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/view-coordination)*