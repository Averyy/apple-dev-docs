# WebContentExtensionConfiguration

**Framework**: BrowserEngineKit  
**Kind**: struct

An opaque configuration structure for a web content extension.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
@MainActor
@preconcurrency struct WebContentExtensionConfiguration
```

#### Overview

See [`WebContentExtension`](webcontentextension.md).

## Relationships

### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol WebContentExtension](webcontentextension.md)
  A protocol for an app extension that manages web content for your browser app.
- [protocol NetworkingExtension](networkingextension.md)
  A protocol for an app extension that manages network connections for your browser app.
- [struct NetworkingExtensionConfiguration](networkingextensionconfiguration.md)
  An opaque configuration structure for a networking extension.
- [protocol RenderingExtension](renderingextension.md)
  A protocol for an app extension that manages graphics rendering for your browser app.
- [struct RenderingExtensionConfiguration](renderingextensionconfiguration.md)
  An opaque configuration structure for a rendering extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/webcontentextensionconfiguration)*