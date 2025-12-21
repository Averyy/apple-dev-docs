# RenderingExtension

**Framework**: BrowserEngineKit  
**Kind**: protocol

An interface for configuring a rendering helper extension process that will carry out operations requiring rendering access on behalf of the browser app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
protocol RenderingExtension : RestrictedSandboxAppliable, AppExtension
```

#### Overview

When you add an object that conforms to `RenderingExtension` in your extension’s Xcode target, annotate the conforming object with `@main` to indicate to `BrowserEngineKit` that this object is the entry point for your extension.

## Topics

### Handling incoming XPC connections
- [func handle(xpcConnection: xpc_connection_t)](renderingextension/handle(xpcconnection:).md)
  Accept or reject an incoming XPC connection.
### Instance Methods
- [func enableFeature(RenderingExtensionFeature)](renderingextension/enablefeature(_:).md)

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [RestrictedSandboxAppliable](restrictedsandboxappliable.md)

## See Also

- [protocol WebContentExtension](webcontentextension.md)
  An interface for configuring a web content helper extension process that will carry web page decoding operations on behalf of the browser app.
- [struct WebContentExtensionConfiguration](webcontentextensionconfiguration.md)
- [protocol NetworkingExtension](networkingextension.md)
  An interface for configuring a networking helper extension process that will carry out networking operations on behalf of the browser app.
- [struct NetworkingExtensionConfiguration](networkingextensionconfiguration.md)
- [struct RenderingExtensionConfiguration](renderingextensionconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingextension)*