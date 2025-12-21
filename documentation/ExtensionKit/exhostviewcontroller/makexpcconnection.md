# makeXPCConnection()

**Framework**: ExtensionKit  
**Kind**: method

Initiates an XPC connection to the app extension’s scene.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+

## Declaration

```swift
@MainActor
func makeXPCConnection() throws -> NSXPCConnection
```

## Mentions

- [Including extension-based UI in your interface](including-extension-based-ui-in-your-interface.md)

#### Discussion

Call this method from the [`hostViewControllerDidActivate(_:)`](exhostviewcontrollerdelegate/hostviewcontrollerdidactivate(_:).md) method to initiate a scene-specific connection to the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller/makexpcconnection())*