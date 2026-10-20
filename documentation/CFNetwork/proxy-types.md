# Proxy Types

**Framework**: CFNetwork  
**Role**: API Collection

Constants that specify the type of proxy.

## Topics

### Constants
- [let kCFProxyTypeNone: CFString](./kcfproxytypenone.md)
  Specifies that no proxy should be used.
- [let kCFProxyTypeAutoConfigurationURL: CFString](./kcfproxytypeautoconfigurationurl.md)
  Specifies that the proxy is determined by an autoconfiguration file at a given URL.
- [let kCFProxyTypeAutoConfigurationJavaScript: CFString](./kcfproxytypeautoconfigurationjavascript.md)
  Specifies that the proxy is determined by a provided autoconfiguration script.
- [let kCFProxyTypeFTP: CFString](./kcfproxytypeftp.md)
  Specifies an FTP proxy.
- [let kCFProxyTypeHTTP: CFString](./kcfproxytypehttp.md)
  Specifies an HTTP proxy.
- [let kCFProxyTypeHTTPS: CFString](./kcfproxytypehttps.md)
  Specifies an HTTPS proxy.
- [let kCFProxyTypeSOCKS: CFString](./kcfproxytypesocks.md)
  Specifies a SOCKS proxy.

## See Also

### Global Proxy Configuration
- [func CFNetworkCopyProxiesForURL(CFURL, CFDictionary) -> Unmanaged<CFArray>](./cfnetworkcopyproxiesforurl%28_,_%29.md)
  Returns the list of proxies that should be used to download a given URL.
- [func CFNetworkCopyProxiesForAutoConfigurationScript(CFString, CFURL, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](./cfnetworkcopyproxiesforautoconfigurationscript%28_,_,_%29.md)
  Executes a proxy autoconfiguration script to determine the best proxy to use to retrieve a specified URL.
- [func CFNetworkExecuteProxyAutoConfigurationScript(CFString, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](./cfnetworkexecuteproxyautoconfigurationscript%28_,_,_,_%29.md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkExecuteProxyAutoConfigurationURL(CFURL, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](./cfnetworkexecuteproxyautoconfigurationurl%28_,_,_,_%29.md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>?](./cfnetworkcopysystemproxysettings%28%29.md)
  Returns a CFDictionary containing the current systemwide internet proxy settings.
- [typealias CFProxyAutoConfigurationResultCallback](./cfproxyautoconfigurationresultcallback.md)
  Callback function called when a proxy autoconfiguration computation has completed.
- [Property Keys](./property-keys.md)
  Keys for calls to property get/set functions such as [`CFReadStreamSetProperty(_:_:_:)`](../CoreFoundation/cfreadstreamsetproperty%28_,_,_%29.md) and [`CFReadStreamCopyProperty(_:_:)`](../CoreFoundation/cfreadstreamcopyproperty%28_,_%29.md).
- [Global Proxy Settings Constants](./global-proxy-settings-constants.md)
  Constants for keys in the global proxy settings dictionary returned by [`CFNetworkCopySystemProxySettings()`](./cfnetworkcopysystemproxysettings%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/proxy-types)*