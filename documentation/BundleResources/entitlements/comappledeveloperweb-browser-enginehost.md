# Web Browser Engine Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that enables your browser app to implement an alternative browser engine.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

#### Discussion

Add this entitlement to your browser app’s code signature to implement an alternative browser engine, which includes separating tasks such as rendering, network traffic, and web content, across dedicated extensions that you develop.

To use the entitlement, request it from Apple. The steps to request the entitlement vary by geographic region:

For more information, see [`Creating browser extensions in Xcode`](https://developer.apple.com/documentation/BrowserEngineKit/creating-browser-extensions-in-xcode).

## See Also

- [Embedded Browser Engine Entitlement](entitlements/com.apple.developer.embedded-web-browser-engine.md)
  An entitlement that enables an app to embed an alternative browser engine.
- [Embedded Browser Engine Association Entitlement](entitlements/com.apple.developer.embedded-web-browser-engine.engine-association.md)
  An entitlement that indicates whether you own the alternative browser engine that your app embeds.
- [com.apple.developer.web-browser-engine.networking](entitlements/com.apple.developer.web-browser-engine.networking.md)
  An entitlement that grants an alternative browser engine’s extension the ability to use the network.
- [com.apple.developer.web-browser-engine.webcontent](entitlements/com.apple.developer.web-browser-engine.webcontent.md)
  An entitlement that grants an alternative browser engine’s extension the ability to manage web content.
- [com.apple.developer.web-browser-engine.rendering](entitlements/com.apple.developer.web-browser-engine.rendering.md)
  An entitlement that grants an alternative browser engine’s extension the ability to render web content.
- [com.apple.developer.memory.transfer_accept](entitlements/com.apple.developer.memory.transfer_accept.md)
  An entitlement that grants an alternative browser engine’s web-content extension the ability to increase memory.
- [com.apple.developer.memory.transfer_send](entitlements/com.apple.developer.memory.transfer_send.md)
  An entitlement that grants an alternative browser engine’s rendering extension the ability to transfer memory.
- [com.apple.developer.web-browser-engine.restrict.notifyd](entitlements/com.apple.developer.web-browser-engine.restrict.notifyd.md)
  An entitlement that restricts access to system notifications to enhance the security of your browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.web-browser-engine.host)*