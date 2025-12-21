# WebContentExtensionConfiguration

**Framework**: BrowserEngineKit  
**Kind**: struct

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
@MainActor
@preconcurrency struct WebContentExtensionConfiguration
```

## Relationships

### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol WebContentExtension](webcontentextension.md)
  An interface for configuring a web content helper extension process that will carry web page decoding operations on behalf of the browser app.
- [protocol NetworkingExtension](networkingextension.md)
  An interface for configuring a networking helper extension process that will carry out networking operations on behalf of the browser app.
- [struct NetworkingExtensionConfiguration](networkingextensionconfiguration.md)
- [protocol RenderingExtension](renderingextension.md)
  An interface for configuring a rendering helper extension process that will carry out operations requiring rendering access on behalf of the browser app.
- [struct RenderingExtensionConfiguration](renderingextensionconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/webcontentextensionconfiguration)*