# NetworkingExtension

**Framework**: BrowserEngineKit  
**Kind**: protocol

A protocol for an app extension that manages network connections for your browser app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
protocol NetworkingExtension : RestrictedSandboxAppliable, AppExtension
```

#### Overview

When you add an object that conforms to this protocol in your extension’s Xcode target, annotate the conforming object with `@main` to indicate to the framework that this object is the entry point for your extension.

## Topics

### Handling incoming XPC connections
- [func handle(xpcConnection: xpc_connection_t)](networkingextension/handle(xpcconnection:).md)
  Accepts or rejects an incoming XPC connection.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [RestrictedSandboxAppliable](restrictedsandboxappliable.md)

## See Also

- [protocol WebContentExtension](webcontentextension.md)
  A protocol for an app extension that manages web content for your browser app.
- [struct WebContentExtensionConfiguration](webcontentextensionconfiguration.md)
  An opaque configuration structure for a web content extension.
- [struct NetworkingExtensionConfiguration](networkingextensionconfiguration.md)
  An opaque configuration structure for a networking extension.
- [protocol RenderingExtension](renderingextension.md)
  A protocol for an app extension that manages graphics rendering for your browser app.
- [struct RenderingExtensionConfiguration](renderingextensionconfiguration.md)
  An opaque configuration structure for a rendering extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/networkingextension)*