# Extension life cycle

**Framework**: BrowserEngineKit

Launch, communicate with, and invalidate browser extensions.

## Topics

### Essentials
- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)
  Coordinate helper processes to efficiently support your browser app.
- [Using XPC to communicate with browser extensions](using-xpc-to-communicate-with-browser-extensions.md)
  Build interprocess communication between your host app and extensions.
- [protocol BEExtensionProcess](beextensionprocess.md)
  A common protocol that creates XPC connections for an extension process.
### Browser extensions
- [protocol WebContentExtension](webcontentextension.md)
  A protocol for an app extension that manages web content for your browser app.
- [struct WebContentExtensionConfiguration](webcontentextensionconfiguration.md)
  An opaque configuration structure for a web content extension.
- [protocol NetworkingExtension](networkingextension.md)
  A protocol for an app extension that manages network connections for your browser app.
- [struct NetworkingExtensionConfiguration](networkingextensionconfiguration.md)
  An opaque configuration structure for a networking extension.
- [protocol RenderingExtension](renderingextension.md)
  A protocol for an app extension that manages graphics rendering for your browser app.
- [struct RenderingExtensionConfiguration](renderingextensionconfiguration.md)
  An opaque configuration structure for a rendering extension.
### Host app representations
- [struct WebContentProcess](webcontentprocess.md)
  A process that manages webpage content in an app extension.
- [struct NetworkingProcess](networkingprocess.md)
  A process that manages network connections in an app extension.
- [struct RenderingProcess](renderingprocess.md)
  A process that manages rendering in an app extension.
### Extension capabilities
- [enum ProcessCapability](processcapability.md)
  Capabilities of a helper extension process.
- [class BEProcessCapability](beprocesscapability-76ijx.md)
  Capabilities of a helper extension process.
- [struct MediaEnvironment](mediaenvironment.md)
  An object that identifies a media playback or streaming environment.
- [class BEMediaEnvironment](bemediaenvironment-15xci.md)
  An object that identifies a media playback or streaming environment.
- [class BEWebContentFilter](bewebcontentfilter.md)
  An object that represents a web content filter.
- [enum RenderingExtensionFeature](renderingextensionfeature.md)
  Features of a rendering extension.

## See Also

- [Creating browser extensions in Xcode](creating-browser-extensions-in-xcode.md)
  Configure your Xcode project to support your alternative browser engine.
- [Extension resources](extension-resources.md)
  Control access to files and memory in browser extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/extension-lifecycle)*