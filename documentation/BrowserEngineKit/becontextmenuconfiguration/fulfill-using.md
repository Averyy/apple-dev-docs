# fulfill(using:)

**Framework**: BrowserEngineKit  
**Kind**: method

Supplies a contextual menu configuration to the system.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func fulfill(using configuration: UIContextMenuConfiguration?) -> Bool
```

#### Return Value

`true` if you fulfill the configuration within the system’s time window; `false` otherwise.

#### Discussion

When the system calls your delegate’s [`contextMenuInteraction(_:configurationForMenuAtLocation:)`](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:configurationformenuatlocation:)) method to request a menu configuration, return a [`BEContextMenuConfiguration`](becontextmenuconfiguration.md) instance, then call this method as soon as you can to provide the actual configuration. The system times out the request after a short delay to keep the UI responsive.

If you don’t call this method before the timeout, the system discards the contextual menu as if you passed `nil`. When you fulfill the configuration, your [`UIContextMenuInteractionDelegate`](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate) uses the `configuration` object you supply to configure the contextual menu — not the [`BEContextMenuConfiguration`](becontextmenuconfiguration.md) instance you pass to [`contextMenuInteraction(_:configurationForMenuAtLocation:)`](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:configurationformenuatlocation:)).

## Parameters

- `configuration`: The calculated configuration for the contextual menu. Pass `nil` to cancel menu presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/becontextmenuconfiguration/fulfill(using:))*