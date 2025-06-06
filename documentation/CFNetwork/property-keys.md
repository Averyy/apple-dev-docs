# Property Keys

**Framework**: CFNetwork

Keys for calls to property get/set functions such as [`CFReadStreamSetProperty(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamSetProperty(_:_:_:)) and [`CFReadStreamCopyProperty(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamCopyProperty(_:_:)).

## Topics

### Constants
- [let kCFProxyAutoConfigurationHTTPResponseKey: CFString](kcfproxyautoconfigurationhttpresponsekey.md)
- [let kCFProxyAutoConfigurationJavaScriptKey: CFString](kcfproxyautoconfigurationjavascriptkey.md)
- [let kCFProxyAutoConfigurationURLKey: CFString](kcfproxyautoconfigurationurlkey.md)
- [let kCFProxyHostNameKey: CFString](kcfproxyhostnamekey.md)
- [let kCFProxyPasswordKey: CFString](kcfproxypasswordkey.md)
- [let kCFProxyPortNumberKey: CFString](kcfproxyportnumberkey.md)
- [let kCFProxyTypeKey: CFString](kcfproxytypekey.md)
- [let kCFProxyUsernameKey: CFString](kcfproxyusernamekey.md)

## See Also

- [func CFNetworkCopyProxiesForURL(CFURL, CFDictionary) -> Unmanaged<CFArray>](cfnetworkcopyproxiesforurl(_:_:).md)
  Returns the list of proxies that should be used to download a given URL.
- [func CFNetworkCopyProxiesForAutoConfigurationScript(CFString, CFURL, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](cfnetworkcopyproxiesforautoconfigurationscript(_:_:_:).md)
  Executes a proxy autoconfiguration script to determine the best proxy to use to retrieve a specified URL.
- [func CFNetworkExecuteProxyAutoConfigurationScript(CFString, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](cfnetworkexecuteproxyautoconfigurationscript(_:_:_:_:).md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkExecuteProxyAutoConfigurationURL(CFURL, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](cfnetworkexecuteproxyautoconfigurationurl(_:_:_:_:).md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>?](cfnetworkcopysystemproxysettings().md)
  Returns a CFDictionary containing the current systemwide internet proxy settings.
- [typealias CFProxyAutoConfigurationResultCallback](cfproxyautoconfigurationresultcallback.md)
  Callback function called when a proxy autoconfiguration computation has completed.
- [Proxy Types](proxy-types.md)
  Constants that specify the type of proxy.
- [Global Proxy Settings Constants](global-proxy-settings-constants.md)
  Constants for keys in the global proxy settings dictionary returned by [`CFNetworkCopySystemProxySettings()`](cfnetworkcopysystemproxysettings().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/property-keys)*