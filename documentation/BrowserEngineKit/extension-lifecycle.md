# Extension lifecycle

**Framework**: BrowserEngineKit

Launch, communicate with, and invalidate browser extensions.

## Topics

### Essentials
- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)
  Coordinate helper processes to efficiently support your browser app.
- [Using XPC to communicate with browser extensions](using-xpc-to-communicate-with-browser-extensions.md)
  Build interprocess communication between your host app and extensions.
### Browser extensions
- [protocol WebContentExtension](webcontentextension.md)
  An interface for configuring a web content helper extension process that will carry web page decoding operations on behalf of the browser app.
- [struct WebContentExtensionConfiguration](webcontentextensionconfiguration.md)
- [protocol NetworkingExtension](networkingextension.md)
  An interface for configuring a networking helper extension process that will carry out networking operations on behalf of the browser app.
- [struct NetworkingExtensionConfiguration](networkingextensionconfiguration.md)
- [protocol RenderingExtension](renderingextension.md)
  An interface for configuring a rendering helper extension process that will carry out operations requiring rendering access on behalf of the browser app.
- [struct RenderingExtensionConfiguration](renderingextensionconfiguration.md)
### Host app representations
- [struct WebContentProcess](webcontentprocess.md)
  An object that represents a running web content extension process.
- [struct NetworkingProcess](networkingprocess.md)
  An object that represents a running browser networking extension process.
- [struct RenderingProcess](renderingprocess.md)
  An object that represents a running browser rendering extension process.
### Extension capabilities
- [enum ProcessCapability](processcapability.md)
  An enumeration that identifies capabilities that a browser app can grant to its extension processes.
- [struct MediaEnvironment](mediaenvironment.md)
  An object that identifies a media playback or streaming environment.

## See Also

- [Creating browser extensions in Xcode](creating-browser-extensions-in-xcode.md)
  Configure your Xcode project to support your alternative browser engine.
- [Extension resources](extension-resources.md)
  Control access to files and memory in browser extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/extension-lifecycle)*