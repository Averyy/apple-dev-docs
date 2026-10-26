# interface

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Type Method

Convenience method for getting an CWInterface object for the default WLAN interface.

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

> **Deprecated**: This method relies on direct access to system sockets, and therefore cannot be used in a sandboxed app. Use the [`interface()`](../cwwificlient/interface%28%29.md) instance method of [`CWWiFiClient`](../cwwificlient.md) instead.

## Declaration

```objc
+ (instancetype) interface;
```

#### Return Value

An CWInterface object.

## See Also

### Getting an interface
- [init(interfaceName: String?)](./init%28interfacename%29.md)
  Convenience method for getting an CWInterface object with the specified name.
- [convenience init(name: String?)](./init%28name%29.md)
  An instance method for obtaining an CWInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/interface)*