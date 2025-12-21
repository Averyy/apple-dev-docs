# Embedded Browser Engine Association Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that indicates whether you own the alternative browser engine that your app embeds.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

#### Discussion

If your app that’s not a web browser embeds an alternative browser engine for in-app browsing, include this entitlement to specify whether you own the embedded alternative browser engine. Also add the [`Embedded Browser Engine Entitlement`](entitlements/com.apple.developer.embedded-web-browser-engine.md).

Apps that set the value to `third-party` can only install on devices in the European Union. Apps that set the value to `first-party` can install on devices in the European Union and Japan.

## See Also

- [Embedded Browser Engine Entitlement](entitlements/com.apple.developer.embedded-web-browser-engine.md)
  An entitlement that enables an app to embed an alternative browser engine.
- [Web Browser Engine Entitlement](entitlements/com.apple.developer.web-browser-engine.host.md)
  An entitlement that enables your browser app to implement an alternative browser engine.
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

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.embedded-web-browser-engine.engine-association)*