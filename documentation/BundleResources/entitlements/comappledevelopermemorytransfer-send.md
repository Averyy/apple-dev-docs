# com.apple.developer.memory.transfer_send

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that grants an alternative browser engine’s rendering extension the ability to transfer memory.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

#### Discussion

To increase the memory allocation of your alternative browser engine’s rendering extension, add this entitlement to its code signature and set the value of this entitlement to your browser app’s bundle ID.

For more information, see [`Attributing memory to a content extension`](https://developer.apple.com/documentation/BrowserEngineKit/attributing-memory-to-a-content-extension).

## See Also

- [Embedded Browser Engine Entitlement](entitlements/com.apple.developer.embedded-web-browser-engine.md)
  An entitlement that enables an app to embed an alternative browser engine.
- [Embedded Browser Engine Association Entitlement](entitlements/com.apple.developer.embedded-web-browser-engine.engine-association.md)
  An entitlement that indicates whether you own the alternative browser engine that your app embeds.
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
- [com.apple.developer.web-browser-engine.restrict.notifyd](entitlements/com.apple.developer.web-browser-engine.restrict.notifyd.md)
  An entitlement that restricts access to system notifications to enhance the security of your browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.memory.transfer_send)*